import requests
import json 
from pathlib import Path
api_url = 'https://www.ebi.ac.uk/interpro/api/protein/uniprot/'

class Protein:
    def __init__(self, accession: str, taxid: int, outdirectory: str):
        self.accession = accession
        self.taxid = taxid
        url = f"{api_url}{self.accession}"
        response = requests.get(url) 
        self.data = response.json()
        Path(outdirectory).mkdir(parents=True, exist_ok=True)
        json.dump(self.data, open(f"{outdirectory}/{self.accession}.json", "w")) 

    def get_taxid(self):
        return self.taxid
    
    def get_accession(self):
        return self.accession

    def __get_metadata(self):
        return self.data["metadata"]

    def get_source_organism_name(self):
        return self.__get_metadata()["source_organism"]["scientificName"]
    
    def get_name(self):
        return self.__get_metadata()["name"]
    
    def get_length(self):
        return self.__get_metadata()["length"]

    def get_sequence(self):
        return self.__get_metadata()["sequence"]
    
    def get_gene(self):
        return self.__get_metadata()["gene"]
    
    def get_source_db(self):
        return self.__get_metadata()["source_database"]
    
    def is_fragment(self):
        return self.__get_metadata()["is_fragment"]
    
    def in_alphafold(self):
        return self.__get_metadata()["in_alphafold"]

