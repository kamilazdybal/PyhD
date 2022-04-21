# This script counts how many bibliography items are included in the .bib file

# User input: ------------------------------------------------------

directory = './'
filename = 'dissertation-bib.bib'

# ------------------------------------------------------------------

n_items = 0
n_articles = 0
n_books = 0
n_inproceedings = 0
n_incollection = 0
n_phdthesis = 0
n_misc = 0

file = open(directory + filename, 'r+')
file_content = file.read()
file_list = file_content.split('\n')

for item in file_list:
    if len(item) != 0:
        if item[0] == '@':
            n_items += 1
        if item[0:8] == '@article':
            n_articles +=1
        if item[0:5] == '@book':
            n_books += 1
        if item[0:14] == '@inproceedings':
            n_inproceedings += 1
        if item[0:13] == '@incollection':
            n_incollection += 1
        if item[0:10] == '@phdthesis':
            n_phdthesis += 1
        if item[0:5] == '@misc':
            n_misc += 1

print('\n' + '-'*40)
print('Total bibliography items:\t' + str(n_items))
if n_articles > 0: print('\tJournal articles:\t' + str(n_articles))
if n_books > 0: print('\tTextbooks:\t\t' + str(n_books))
if n_inproceedings > 0: print('\tIn proceedings:\t\t' + str(n_inproceedings))
if n_incollection > 0: print('\tIn collection:\t\t' + str(n_incollection))
if n_phdthesis > 0: print('\tPhD theses:\t\t' + str(n_phdthesis))
if n_misc > 0: print('\tMiscellaneous:\t\t' + str(n_misc))
print('-'*40 + '\n')

file.close()
