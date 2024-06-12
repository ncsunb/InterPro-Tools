
from ProteinFamily import ProteinFamily
import re 

ipr_accession_re = r"IPR\d+"
while True:
    ipr_accession_nums = input("Enter the InterPro accessions for the protein family/domain, then hit enter.\n(If there are multiple separate them by spaces): ").split()
    arg_count = len(ipr_accession_nums)
    ipr_accession_nums = [accession.strip() for accession in ipr_accession_nums if re.match(ipr_accession_re, accession.upper())]
    if len(ipr_accession_nums) == arg_count:
        break
    else:
        print("Please ensure all provided accessions are InterPro accessions, e.g., IPR012345\n")

while True:
    try:
        taxon_id_nums = input("\nEnter the taxon ID(s) for the taxon you wish to search, then hit enter\n(If there are multiple separate them by spaces): ").split()
        taxon_id_nums = [int(taxon_id.strip()) for taxon_id in taxon_id_nums]
        break
    except:
        print("Please provide a valid integer response.")

for ian in ipr_accession_nums:
    for tid in taxon_id_nums:
        protfam_domain = ProteinFamily(ian, tid, "Output")
        protfam_domain.get_match_subsequences()