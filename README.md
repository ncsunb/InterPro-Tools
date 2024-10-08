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
**If you have Windows**, 
a. Click the download button at the top of [Python](https://www.python.org/downloads/)   
b. Open the downloaded installer, check off the option about adding Python to PATH.  
c. Click Install.  
d. Close the Command Prompt application in order for the new changes to take effect.  
e. To check that it worked, open the Command Prompt application, type "python --version", and hit enter. If it tells you the version instead of giving you an error about not recognizing it, it worked.


2. You must have the Python [requests](https://pypi.org/project/requests/) package installed. You may use pip to install this by pasting this command into your terminal: `pip3 install requests`.   
**You may wish to do this inside a virtual environment** (or if you use HomeBrew it may instruct you to use a virtual environment before attempting to install things with pip) by pasting these commands into your terminal/command prompt:  
**macOS instructions**:
```
cd ~/Desktop/[YOUR PATH TO YOUR FOLDER FOR THIS PROJECT]

mkdir venv # make a directory for your virtual environment

python3 -m venv venv # Create your virtual environment inside the venv directory

source venv/bin/activate # Activate your virtual environment (bash/zsh shell)

pip3 install requests
```
**Windows instructions**:
```
cd C:\Usr\[Name]\[YOUR PATH TO YOUR FOLDER FOR THIS PROJECT]

mkdir venv  # make a directory for your virtual environment

python -m venv venv  # Create your virtual environment inside the venv directory

venv\Scripts\activate.bat  # Activate your virtual environment (cmd.exe shell)
# OR IF the above command does NOT work try:
venv\Scripts\Activate.ps1  # Activate your virtual environment (PowerShell)

pip3 install requests
```
That should be it for software this tool requires!
When you wish to deactivate your virtual environment _after you are done using it_, use this command:
```
deactivate
```

# Downloading this project
1. Start by installing [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), if you haven't already. __When installing on Windows__, download the file from that link, double click it and then just use the default values for all the options. You don't care about having the GUI or the release notes, so don't worry about that.

2. On Windows only, in the start menu search system environment variables, open that.  Click environment variables in the bottom right. Select Path from the bottom box, for _system environment variables_, and click edit. Click new and add 'C:\Program Files\Git\cmd' and do the same thing for this 'C:\Program Files\Git\bin'. Click OK and leave the app. If you have a command prompt window open, close it for the changes to take effect.

3. From the terminal, navigate (using `cd path-of-your-folder-where-you-want-it`, replacing path-of-your-folder-where-you-want-it with the actual path) to the directory you wish to download this project to. 

4. Paste the following command in your terminal `git clone https://github.com/ncsunb/InterPro-Tools.git`

That's it!

# Usage
To run this program

1. Navigate to the folder containing the files for this project via the terminal (use `cd path-where-you-downloaded-this-project/InterPro-Tools/` or, if you are on Windows and your filepaths use backslashes instead of forward slashes, use `cd path-where-you-downloaded-this-project\InterPro-Tools\`), if you haven't already.

2. Activate your virtual environment (**macOS:** `source path-to-your-venv-folder/venv/bin/activate`  **Windows:** `path-to-your-venv-folder\venv\Scripts\activate.bat`), if you haven't already.

3. Paste this command into your terminal **macOS:** `python3 Main.py` / **Windows:** `python Main.py` (or press 'Run' if you have it open in VSCode or another IDE).

In the terminal you will see a prompt to enter the InterPro accesssion for the protein family / Domain. You can search your protein family / Domain of interest on [InterPro](https://www.ebi.ac.uk/interpro/search/text/) and find the InterPro accession in the results (the format is like IPR012345)
```
Enter the InterPro accessions for the protein family/domain, then hit enter.
(If there are multiple separate them by spaces): 
```
Enter your InterPro protein family / domain accession numbers here, separated by a space, then hit enter.

You will then be prompted to enter the taxon ID(s) for which you want to search for matching proteins from. You can find those by searching your taxon on [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy)  (click on your matching result, then click on it again on the next page and you should see the Taxonomy ID)  
**NOTE: InterPro does not seem to show matches for high level taxon like kingdoms.** If this program is giving you an error, to check if there are any results paste this into a browser https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/InterPro/IPR000770/taxonomy/uniprot/3042 but replace 3042 with your taxon ID and IPR000770 with your domain/protein family accession.
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

You probably don't care about any of the files ending with .json. The only file you care about is the subsequence matches, which contains the fasta format subsequence matches for the annotated domain/protein family in your taxon.