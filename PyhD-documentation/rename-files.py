from os import listdir
from os import rename
from os.path import isfile, isdir, join

directory = '/Users/kamilazdybal/GitLab/csv/'

count_files = 0

files = [f for f in listdir(directory) if isfile(join(directory, f))]

for file in files:

    if file[0:4] == 'auto':

        count_files = count_files + 1

        old_file_name = r'' + directory + file
        new_file_name = r'' + directory + 'INFO-TO-BE-ADDED-' + file
        rename(old_file_name, new_file_name)
        print(old_file_name)
        print(new_file_name)
        print()

print('\n' + '-'*60)
print('Renamed ' + str(count_files) + ' files.\n')
