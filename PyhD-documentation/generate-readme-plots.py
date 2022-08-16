from os import listdir
from os.path import isfile, join

# User input: ------------------------------------------------------

directory = '/Users/kamilazdybal/GitLab/documentation/'
graphics_extensions = ['png']

# ------------------------------------------------------------------

plots = [f for f in listdir(directory) if isfile(join(directory, f))]

markdown_file = open(directory + 'README.md', 'w+')

markdown_file.write("# Plots\n\n")

for plot in plots:

    plot_list = plot.split('.')

    if plot_list[-1] in graphics_extensions:

        markdown_file.write('![Screenshot](' + plot + ')\n\n')

markdown_file.close()

print('\nREADME.md generated in:\n' + directory + '\n')
