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
        self._pdbid_list = [pdbid for pdbid in pdbid_list]
        self._class_dict = {}
        self._architecture_dict = {}
        self._topology_dict = {}
        self._homologous_superfamily_dict = {}

    def get_cath_info(self):
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
                cath_data = json_data['data']['polymer_entity_instances'][0][
                    'rcsb_polymer_instance_annotation'][0]['annotation_lineage']
                cath_found = False
                for i in range(len(json_data['data']['polymer_entity_instances'][0]['rcsb_polymer_instance_annotation'])):
                    if json_data['data']['polymer_entity_instances'][0]['rcsb_polymer_instance_annotation'][i]['type'] == 'CATH':
                        self._class_dict.setdefault(
                            f"Class {cath_data[0]['id']} ({cath_data[0]['name']})", 0)
                        self._class_dict[
                            f"Class {cath_data[0]['id']} ({cath_data[0]['name']})"] += 1
                        self._architecture_dict.setdefault(
                            f"Architecture {cath_data[1]['id']} ({cath_data[1]['name']})", 0)
                        self._architecture_dict[
                            f"Architecture {cath_data[1]['id']} ({cath_data[1]['name']})"] += 1
                        self._topology_dict.setdefault(
                            f"Topology {cath_data[2]['id']} ({cath_data[2]['name']})", 0)
                        self._topology_dict[
                            f"Topology {cath_data[2]['id']} ({cath_data[2]['name']})"] += 1
                        self._homologous_superfamily_dict.setdefault(
                            f"Homologous Superfamily {cath_data[3]['id']} ({cath_data[3]['name']})", 0)
                        self._homologous_superfamily_dict[
                            f"Homologous Superfamily {cath_data[3]['id']} ({cath_data[3]['name']})"] += 1
                        cath_found = True
                if cath_found == False:
                    print(f"CATH Hierarchy Data not found for {pdbid}")
            except:
                print(f"PDBID: {pdbid} does not exist")

    def convert_dictionaries_to_dataframes(self):
        self._class_df = pd.DataFrame.from_dict(
            data=self._class_dict, orient='index', columns=['Count'])
        self._architecture_dict = pd.DataFrame.from_dict(
            data=self._architecture_dict, orient='index', columns=['Count'])
        self._topology_dict = pd.DataFrame.from_dict(
            data=self._topology_dict, orient='index', columns=['Count'])
        self._homologous_superfamily_dict = pd.DataFrame.from_dict(
            data=self._homologous_superfamily_dict, orient='index', columns=['Count'])

    def convert_dfs_to_percentages(self):
        grouped_dfs = (self._class_df, self._architecture_dict,
                       self._topology_dict, self._homologous_superfamily_dict)
        for df in grouped_dfs:
            df['Percentage'] = df['Count'].divide(int(df.sum()))
            print(df)


def main():
    example_pdbid_list = ['2BE3.A', '2BE4.A',
                          '4BN2.A', '4B8Y.A', '5B8A.A', '7C6D.A', '7C2A.A', '2A1A.A', '5AB2.A', '6CE1.A']
    proteins = ProteinStructures(example_pdbid_list)
    proteins.get_cath_info()
    proteins.convert_dictionaries_to_dataframes()
    proteins.convert_dfs_to_percentages()
    # print('Counts:', '\n')
    # print(proteins._class_dict, '\n')
    # print(proteins._architecture_dict, '\n')
    # print(proteins._topology_dict, '\n')
    # print(proteins._homologous_superfamily_dict, '\n')
    pass


if __name__ == '__main__':
    main()
