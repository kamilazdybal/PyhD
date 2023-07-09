# This script lists all bibliography items tags in the .bib file

# User input: ------------------------------------------------------

directory = './'
filename = 'bibliography.bib'

# ------------------------------------------------------------------

import re

file = open(directory + filename, 'r')
file_content = file.read()
file_list = file_content.split('\n')

for item in file_list:
    
    match = re.search(r'@.*\{(.*),', item)
    
    if match is not None:
        
        tag = match.group(1)
        print(tag)

# ------------------------------------------------------------------