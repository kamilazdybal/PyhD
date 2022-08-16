import nbformat
from urllib.request import urlopen

url = 'https://github.com/kamilazdybal/multipy/raw/main/docs/tutorials/non-reacting-stefan-tube-mole-fractions.ipynb'
response = urlopen(url).read().decode()
response[0:60] + ' ...'

notebook = nbformat.reads(response, as_version=4)
notebook.cells[0]
