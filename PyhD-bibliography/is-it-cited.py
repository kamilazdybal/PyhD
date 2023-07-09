# This script tells you which bibliography items in the .bib file have or have not been cited in the .tex source file

# User input: ------------------------------------------------------

directory = './'
tex_filename = 'dissertation.tex'
bib_filename = 'dissertation-bib.bib'

# ------------------------------------------------------------------

import re

bib_file = open(directory + bib_filename, 'r+')
bib_file_content = bib_file.read()
bib_file_list = bib_file_content.split('\n')
bib_tags_list = []
count_not_used = 0
count_used = 0

for item in bib_file_list:
    if len(item) != 0:
        if item[0] == '@':
            split_item = item.split('{')
            bib_tag = split_item[1][0:-1]
            bib_tags_list.append(bib_tag)

bib_tags_list = list(set(bib_tags_list))

tex_file = open(directory + tex_filename, 'r+')
tex_file_content = tex_file.read()
tex_file_list = re.split('[{, }]+', tex_file_content)

print('\n' + '-'*40)
for tag in sorted(bib_tags_list):
    if tag not in tex_file_list:
        print('Citation not used: ' + tag)
        count_not_used += 1
print('\tTOTAL NOT USED: ' + str(count_not_used))
print('-'*40 + '\n')

print('\n' + '-'*40)
for tag in sorted(bib_tags_list):
    if tag in tex_file_list:
        print('Citation used: ' + tag)
        count_used += 1
print('\tTOTAL USED: ' + str(count_used))
print('-'*40 + '\n')

bib_file.close()
tex_file.close()

# ------------------------------------------------------------------
