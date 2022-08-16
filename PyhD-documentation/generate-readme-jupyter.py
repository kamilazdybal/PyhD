from os import listdir
from os.path import isfile, join

# User input: ------------------------------------------------------

directory = '/Users/kamilazdybal/GitLab/notebooks/'

# ------------------------------------------------------------------

files = [f for f in listdir(directory) if isfile(join(directory, f))]

markdown_file = open(directory + 'README.md', 'w+')

markdown_file.write("# Jupyter notebooks\n\n")

for file in files:

    file_list = file.split('.')

    if file_list[-1] == 'ipynb':

        markdown_file.write('- [`' + file_list[0] + '` Jupyter notebook](' + file + ')\n\n')

markdown_file.close()

print('\nREADME.md generated in:\n' + directory + '\n')
