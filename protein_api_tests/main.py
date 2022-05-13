import argparse
from cgi import test
from traceback import print_tb
import requests
import json

# [ ] Add shell arguments
# [ ] Add parser to pull out pdbids used in training set
# [ ] Make sure to check all chains in PDBID (ie. starting at A and going through each chain)


class ProteinStructures():
    def __init__(self, pdbid_list):
        self._pdbid_list = [pdbid for pdbid in pdbid_list]
        self._class = {}
        self._architecture = {}
        self._topology = {}
        self._homologous_superfamily = {}

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
                        self._class.setdefault(
                            f"Class {cath_data[0]['id']} ({cath_data[0]['name']})", 0)
                        self._class[
                            f"Class {cath_data[0]['id']} ({cath_data[0]['name']})"] += 1
                        self._architecture.setdefault(
                            f"Arch {cath_data[1]['id']} ({cath_data[1]['name']})", 0)
                        self._architecture[
                            f"Arch {cath_data[1]['id']} ({cath_data[1]['name']})"] += 1
                        self._topology.setdefault(
                            f"Top {cath_data[2]['id']} ({cath_data[2]['name']})", 0)
                        self._topology[
                            f"Top {cath_data[2]['id']} ({cath_data[2]['name']})"] += 1
                        self._homologous_superfamily.setdefault(
                            f"Hom {cath_data[3]['id']} ({cath_data[3]['name']})", 0)
                        self._homologous_superfamily[
                            f"Hom {cath_data[3]['id']} ({cath_data[3]['name']})"] += 1
                        cath_found = True
                if cath_found == False:
                    print(f"CATH Hierarchy Data not found for {pdbid}")
            except:
                print(f"PDBID: {pdbid} does not exist")


def main():
    example_pdbid_list = ['2BE3.A', '2BE4.A',
                          '4BN2.A', '4B8Y.A', '5B8A.A', '7C6D.A', '7C2A.A', '2A1A.A', '5AB2.A', '6CE1.A']
    proteins = ProteinStructures(example_pdbid_list)
    proteins.get_cath_info()
    print('Counts:', '\n')
    print(proteins._class, '\n')
    print(proteins._architecture, '\n')
    print(proteins._topology, '\n')
    print(proteins._homologous_superfamily, '\n')
    pass


if __name__ == '__main__':
    main()
