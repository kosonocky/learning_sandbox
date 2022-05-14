import argparse
from cgi import test
from curses.panel import top_panel
from traceback import print_tb
import requests
import json
import pandas as pd

# [ ] Add shell arguments
# [ ] Add parser to pull out pdbids used in training set
# [ ] Make sure to check all chains in PDBID (ie. starting at A and going through each chain)


class ProteinStructures():
    def __init__(self, pdbid_list):
        self._pdbid_list = [f'{pdbid}.A' for pdbid in pdbid_list]
        self._level_0_dict = {}
        self._level_1_dict = {}
        self._level_2_dict = {}
        self._level_3_dict = {}
        self._structure_classification_translation_dict = {
            'SCOP_level_0': 'Class',
            'SCOP_level_1': 'Fold',
            'SCOP_level_2': 'Superfamily',
            'SCOP_level_3': 'Family',
            'CATH_level_0': 'Class',
            'CATH_level_1': 'Architecture',
            'CATH_level_2': 'Topology',
            'CATH_level_3': 'Homologous_Superfamily'
        }

    def get_structure_classification_info(self, classification_type="CATH"):
        self._classification_type = classification_type
        for pdbid in self._pdbid_list:
            try:
                url = "https://data.rcsb.org/graphql"
                query = """{
                        polymer_entity_instances(instance_ids: ["%s"]) {
                            # rcsb_id
                            rcsb_polymer_instance_annotation{
                            type
                            annotation_lineage {
                                id
                                name
                                    }
                                }
                            }
                        }""" % pdbid
                r = requests.post(url, json={'query': query})
                json_data = json.loads(r.text)
                structure_classification_found = False

                for i in range(len(json_data['data']['polymer_entity_instances'][0]['rcsb_polymer_instance_annotation'])):
                    if json_data['data']['polymer_entity_instances'][0]['rcsb_polymer_instance_annotation'][i]['type'] == classification_type:
                        print(
                            f"{classification_type} Data found for {pdbid}   Analyzing now!")
                        structure_data = json_data['data']['polymer_entity_instances'][0][
                            'rcsb_polymer_instance_annotation'][i]['annotation_lineage']
                        self._level_0_dict.setdefault(
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_0']} {structure_data[0]['id']} ({structure_data[0]['name']})", 0)
                        self._level_0_dict[
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_0']} {structure_data[0]['id']} ({structure_data[0]['name']})"] += 1
                        self._level_1_dict.setdefault(
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_1']} {structure_data[1]['id']} ({structure_data[1]['name']})", 0)
                        self._level_1_dict[
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_1']} {structure_data[1]['id']} ({structure_data[1]['name']})"] += 1
                        self._level_2_dict.setdefault(
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_2']} {structure_data[2]['id']} ({structure_data[2]['name']})", 0)
                        self._level_2_dict[
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_2']} {structure_data[2]['id']} ({structure_data[2]['name']})"] += 1
                        self._level_3_dict.setdefault(
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_3']} {structure_data[3]['id']} ({structure_data[3]['name']})", 0)
                        self._level_3_dict[
                            f"{self._structure_classification_translation_dict[f'{classification_type}_level_3']} {structure_data[3]['id']} ({structure_data[3]['name']})"] += 1
                        self._pdbid_list += [
                            f'{pdbid[:-1]}{chr(ord(pdbid[-1:])+1)}']
                        structure_classification_found = True
                if structure_classification_found == False:
                    print(
                        f"{classification_type} Data not found for {pdbid}")
            except:
                print(f"PDBID: {pdbid} does not exist")

    def convert_dictionaries_to_dataframes(self):
        self._level_0_df = pd.DataFrame.from_dict(
            data=self._level_0_dict, orient='index', columns=['Count'])
        self._level_1_df = pd.DataFrame.from_dict(
            data=self._level_1_dict, orient='index', columns=['Count'])
        self._level_2_df = pd.DataFrame.from_dict(
            data=self._level_2_dict, orient='index', columns=['Count'])
        self._level_3_df = pd.DataFrame.from_dict(
            data=self._level_3_dict, orient='index', columns=['Count'])

    def convert_dfs_to_percentages(self):
        grouped_dfs = (self._level_0_df, self._level_1_df,
                       self._level_2_df, self._level_3_df)
        for df in grouped_dfs:
            df['Percentage'] = df['Count'].divide(int(df.sum()))

    def export_dfs(self):
        try:
            grouped_dfs = (self._level_0_df, self._level_1_df,
                           self._level_2_df, self._level_3_df)
            for count, df in enumerate(grouped_dfs):
                df.to_csv(
                    f'./results/{self._classification_type}_{self._structure_classification_translation_dict[f"{self._classification_type}_level_{count}"]}.csv')
        except Exception as ex:
            print(f"Cannot export dataframes to csv | {ex} {ex.args}")


def main():
    example_pdbid_list = ['2BE3', '2BE4', '6B2A', '6BN2', '7B1M', '1B4Y', '4Y2N',
                          '4BN2', '4B8Y', '5B8A', '7C6D', '7C2A', '2A1A', '5AB2', '6CE1', '4B2A', '4B1A']
    proteins = ProteinStructures(example_pdbid_list)
    # print(proteins._pdbid_list)
    proteins.get_structure_classification_info(
        classification_type="CATH")
    proteins.convert_dictionaries_to_dataframes()
    proteins.convert_dfs_to_percentages()
    proteins.export_dfs()


if __name__ == '__main__':
    main()
