
import requests
import json 
from Protein import Protein
from pathlib import Path

api_url = 'https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/InterPro/'
query_path = f"/taxonomy/uniprot/"

class ProteinFamily:
    def __init__(self, ipr_accession: str, query_taxon_id: int, outdirectory: str):
        self.accession = ipr_accession
        self.query_taxon_id = query_taxon_id

        url = f"{api_url}{self.accession}/{query_path}{query_taxon_id}"
        response = requests.get(url) 
        if response.status_code != response.ok:
            self.data = response.json()

            self.outdirectory = f"{outdirectory}/{self.accession}_{self.query_taxon_id}"

            Path(self.outdirectory).mkdir(parents=True, exist_ok=True)
            outfile = open(f"{self.outdirectory}/{self.accession}.json", "w")
            json.dump(self.data, outfile) 

            self.proteins = None
            self.entry_matches = None
        else:
            raise Exception(f"** HTTP Response Code {response.status_code} from {url}")

    def __retrieve_entry_matches(self):
        print(f"\nRetrieving Entries for {self.accession} in taxid {self.query_taxon_id}...")
        entry_match_dict = dict()
        
        # emulating a 'do while' loop with 'True' condition and conditional break statement
        next_data = self.data
        while True:
            # get the accession for each protein result 
            for prot in next_data["results"]:
                accession = prot["metadata"]["accession"]
                # Record the accession number and the sequence matches
                taxa = prot["taxa"]
                entries = prot["entries"]
                taxid_entry_list = [(taxa[i]["lineage"][-1], entries[i]) for i in range(0, len(entries))]
                entry_match_dict[accession] = taxid_entry_list
            # get the response from the next URL
            next_url = next_data["next"]
            if next_url is None:
                break
            next_response = requests.get(next_url) 
            next_data = next_response.json()

        self.entry_matches = entry_match_dict

    def get_entry_matches(self):
        if self.entry_matches is None:
            self.__retrieve_entry_matches()
        return self.entry_matches
        
    def __get_proteins(self):
        proteins = dict()
        entry_dict = self.get_entry_matches()
        print(f"\nRetrieving Proteins for {self.accession} in taxid {self.query_taxon_id}...")
        for accession, taxid_entry_list in entry_dict.items():
            for taxid, entries in taxid_entry_list:
                proteins[accession] = Protein(accession, taxid, f"{self.outdirectory}/proteins/")
        self.proteins = proteins
    
    def get_proteins(self):
        if self.proteins is None:
            self.__get_proteins()
        return self.proteins
    
    def __extract_sequence_matches_from_protein(self, prot_accession):
        taxid_entry_list = self.get_entry_matches().get(prot_accession, None)
        if taxid_entry_list is None: return None

        matches_from_sequence = []

        for taxid, entry in taxid_entry_list:
            for prot_loc in entry["entry_protein_locations"]:
                for fragment in prot_loc["fragments"]:
                    start_idx = fragment["start"] - 1 # inclusive when slicing, start position indexes from 1 
                    end_idx = fragment["end"] # exclusive when slicing, but python indexes from 0, so it will be included
                    # TODO consider whether something should be done if results are continuous, or N/C terminal discontinuous

                    seq = self.get_proteins()[prot_accession].get_sequence()

                    subseq = seq[start_idx:end_idx]
                    matches_from_sequence.append(subseq)
        
        return matches_from_sequence

    def get_match_subsequences(self):
        proteins = self.get_proteins()
        outfile = open(f"{self.outdirectory}/{self.accession}_{self.query_taxon_id}_subsequence_matches.fasta", "w")


        print(f"\nFinding Protein Subsequence Matches for {self.accession} in taxid {self.query_taxon_id}...")
        for accession, prot in proteins.items():
            subseqs = self.__extract_sequence_matches_from_protein(accession)
            for i in range(0, len(subseqs)):
                seq = subseqs[i]
                outfile.write(f">{prot.get_accession()}|{prot.get_source_db()}|{prot.get_name()}|{prot.get_source_organism_name()}|taxID:{prot.get_taxid()}\n{seq}")
                if i < len(subseqs) - 1:
                    outfile.write("\n")
            


