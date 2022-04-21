# This script tells you which bib items tags have been defined multiple times in the .bib file

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

if len(bib_tags_list) != len(set(bib_tags_list)):

    duplicates = set([i for i in bib_tags_list if bib_tags_list.count(i) > 1])

    print('\n' + '-'*40)
    for item in sorted(duplicates):
        print(item)

    print('\t' + str(len(duplicates)) + ' DUPLICATE TAGS FOUND.')
    print('-'*40 + '\n')

else:

    print('\n' + '-'*40)
    print('NO DUPLICATE TAGS FOUND.')
    print('-'*40 + '\n')

bib_file.close()
