# This script counts how many bibliography items are included in the .bib file

# User input: ------------------------------------------------------

directory = './'
filename = 'bibliography.bib'

# ------------------------------------------------------------------

import re

file = open(directory + filename, 'r')
file_content = file.read()
file_list = file_content.split('\n')

entry_types = ['article',
               'book',
               'booklet',
               'inbook',
               'incollection',
               'inproceedings',
               'manual',
               'mastersthesis',
               'misc',
               'phdthesis',
               'proceedings',
               'techreport',
               'unpublished']

count_entry_types = {}

for i in entry_types:
    count_entry_types[i] = 0
    
for item in file_list:
    match = re.search(r'@(.*)\{', item)
    if match is not None:
        
        entry_type = match.group(1)
        count_entry_types[entry_type] += 1

n_items = sum(count_entry_types.values())

file.close()

print('Total bibliography items: ' + str(n_items))
print('- '*20)
for entry_type, value in count_entry_types.items():
    print('%20s%i' % (entry_type + ': ', value) )
print('- '*20)

# ------------------------------------------------------------------
