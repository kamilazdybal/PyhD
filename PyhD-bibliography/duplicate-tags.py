# This script finds duplicate bibliography items tags in the .bib file

# User input: ------------------------------------------------------

directory = './'
filename = 'bibliography.bib'

# ------------------------------------------------------------------

import re

file = open(directory + filename, 'r')
file_content = file.read()
file_list = file_content.split('\n')

tags_list = []

for item in file_list:
    
    match = re.search(r'@.*\{(.*),', item)
    
    if match is not None:
        
        tag = match.group(1)
        tags_list.append(tag)

file.close()

if len(tags_list) != len(set(tags_list)):
    
    duplicates = set([item for item in tags_list if tags_list.count(item) > 1])
 
    print('Duplicate tags found: ' + str(len(duplicates)))
    
    print('- '*20)
    for item in duplicates:
        print(item)
    print('- '*20)
    
else:
    
    print('No duplicates found.')

# ------------------------------------------------------------------
