# Purpose
This project was made for the purpose of easily downloading fasta files from InterPro for multiple Protein families/Domains. Also, this program records only the matching subsequence of the proteins in each record of the fasta file, rather than the default, which is the whole sequence.

# Requirements
1. You must have [Python](https://www.python.org/downloads/) installed.  
_If you have macOS_ you may install [Python](https://docs.brew.sh/Homebrew-and-Python) through the [HomeBrew](https://brew.sh/) package manager by pasting these commands into your terminal : 
```
# install the HomeBrew package manager if you do not already have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install python
brew install python3
```


2. You must have the Python [requests](https://pypi.org/project/requests/) package installed. You may use pip to install this by pasting this command into your terminal: `pip3 install requests`.   
You may wish to do this inside a virtual enviroment (or if you use HomeBrew it may instruct you to use a virtual environment before attempting to install things with pip) by pasting these commands into your terninal:
```
mkdir venv # make a directory for your virtual environment

python3 -m venv venv
source venv/bin/activate
# or if you are on Windows and your filepaths use backslashes instead of forward slashes `venv\bin\activate`

pip3 install requests
```
```
# when you which to deactivate your virtual environment after you are done using it, use this command:
deactivate
```
That should be it!

# Downloading this project
1. Start by installing [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), if you haven't already.

2. From the terminal, navigate (using `cd path-of-your-folder-where-you-want-it`, replacing path-of-your-folder-where-you-want-it with the actual path) to the directory you wish to download this project to. 

3. Paste the following command in your terminal `git clone https://github.com/ncsunb/InterPro-Tools.git`

That's it!

# Usage
To run this program

1. Navigate to the folder containing the files for this project via the terminal (use `cd path-where-you-downloaded-this-project/InterPro-Tools/` or, if you are on Windows and your filepaths use backslashes instead of forward slashes, use `cd path-where-you-downloaded-this-project\InterPro-Tools\`), if you haven't already.

2. Activate your virtual environment (`source path-to-your-venv-folder/venv/bin/activate` or if you are on Windows and your filepaths use backslashes instead of forward slashes `source path-to-your-venv-folder\venv\bin\activate`), if you haven't already.

3. Paste this command into your terminal `python3 Main.py` (or press 'Run' if you have it open in VSCode or another IDE).

In the terminal you will see a prompt to enter the InterPro accesssion for the protein family / Domain. You can search your protein family / Domain of interest on [InterPro](https://www.ebi.ac.uk/interpro/search/text/) and find the InterPro accession in the results (the format is like IPR012345)
```
Enter the InterPro accessions for the protein family/domain, then hit enter.
(If there are multiple separate them by spaces): 
```
Enter your InterPro protein family / domain accession numbers here, separated by a space, then hit enter.

You will then be prompted to enter the taxon ID(s) for which you want to search for matching proteins from.
```
Enter the InterPro accessions for the protein family/domain, then hit enter.
(If there are multiple separate them by spaces): IPR000770 IPR010919

Enter the taxon ID(s) for the taxon you wish to search, then hit enter
(If there are multiple separate them by spaces): 
```

After entering the taxon IDs, the program will start searching for matches. 

You will see small progress updates on the terminal letting you know what task the program is currently working on. 

Since there may be many results, it may take a few minutes to complete (or longer if you have entered many or large taxons and protein families in your query).
```
Enter the InterPro accessions for the protein family/domain, then hit enter.
(If there are multiple separate them by spaces): IPR000770 IPR010919

Enter the taxon ID(s) for the taxon you wish to search, then hit enter
(If there are multiple separate them by spaces): 3166

Retrieving Entries for IPR000770 in taxid 3166...

Retrieving Proteins for IPR000770 in taxid 3166...

Finding Protein Subsequence Matches for IPR000770 in taxid 3166...

Retrieving Entries for IPR010919 in taxid 3166...

Retrieving Proteins for IPR010919 in taxid 3166...

Finding Protein Subsequence Matches for IPR010919 in taxid 3166...
```

Once the program is finished, you should see the results have been written to files in the folder `Output/`.


The naming convention used for these files is `Protein Family Accession_taxon ID` for the folders and the subsequence match fasta files, and simply the accession number followed by the file extension for the JSON API responses containing the information about the protein family matches and the proteins themselves.