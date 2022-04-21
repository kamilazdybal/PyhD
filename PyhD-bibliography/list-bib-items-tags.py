# This script prints the tags to all bibliography items in the .bib file in alphabetic order

# User input: ------------------------------------------------------

directory = './'
bib_filename = 'dissertation-bib.bib'

# ------------------------------------------------------------------

bib_file = open(directory + bib_filename, 'r+')
bib_file_content = bib_file.read()
bib_file_list = bib_file_content.split('\n')
bib_tags_list = []

for item in bib_file_list:
    if len(item) != 0:
        if item[0] == '@':
            split_item = item.split('{')
            bib_tag = split_item[1][0:-1]
            bib_tags_list.append(bib_tag)

bib_tags_list = list(set(bib_tags_list))

print('\n' + '-'*40)
for item in sorted(bib_tags_list):
    print(item)
print('-'*40 + '\n')

bib_file.close()
