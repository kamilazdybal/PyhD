# This script renames files that have format '(YYYY) Publication TITLE' to lower case '(YYYY) Publication title'

from os import listdir
from os import rename
from os.path import isfile, isdir, join

# User input: ------------------------------------------------------

path = './'

# ------------------------------------------------------------------

directories = [join(path, o) for o in listdir(path)
                    if isdir(join(path,o))]

count_files = 0

for directory in directories:
    directory = directory + '/'
    files = [f for f in listdir(directory) if isfile(join(directory, f))]

    for file in files:
        if file[0] == '(' and file[5] == ')' and any([el.isupper() for el in list(file[8::])]):

            count_files = count_files + 1

            old_file_name = r'' + directory + file
            new_file_name = r'' + directory + file[0:7] + file[7:8].upper() + file[8::].lower()
            rename(old_file_name, new_file_name)
            print(file)
            print(file[0:7] + file[7:8].upper() + file[8::].lower())
            print()

print('\n' + '-'*60)
print('Renamed ' + str(count_files) + ' files.\n')
