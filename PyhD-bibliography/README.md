# 🎓 Python scripts to manage your bibliography

## Count the number of bibliography items in a `.bib` file

► [`count-bibliography-items.py`](count-bibliography-items.py)

Running this script on your `.bib` file will print something like this:

```
Total bibliography items: 8
- - - - - - - - - - - - - - - - - - - - 
           article: 4
              book: 2
           booklet: 0
            inbook: 0
      incollection: 0
     inproceedings: 1
            manual: 0
     mastersthesis: 0
              misc: 0
         phdthesis: 1
       proceedings: 0
        techreport: 0
       unpublished: 0
- - - - - - - - - - - - - - - - - - - - 
```

The only thing you need to set in the script is the path to your `.bib` file:

```python
directory = './'
filename = 'bibliography.bib'
```

## Print the tags to all bibliography items in a `.bib` file

► [`list-bib-items-tags.py`](list-bib-items-tags.py)

Running this script on your `.bib` file will print something like this:

```
breiman2001statistical
lusch2018deep
kobak2019art
nilsson2007regression
goodfellow2016deep
zdybal2023dissertation
breiman2001statistical
goodfellow2016deep
```

The only thing you need to set in the script is the path to your `.bib` file:

```python
directory = './'
bib_filename = 'bibliography.bib'
```

## Find duplicate bibliography items tags in a `.bib` file

► [`duplicate-tags.py`](duplicate-tags.py)

Running this script on your `.bib` file will print something like this:

```
Duplicate tags found: 2
- - - - - - - - - - - - - - - - - - - - 
goodfellow2016deep
breiman2001statistical
- - - - - - - - - - - - - - - - - - - - 
```

The only thing you need to set in the script is the path to your `.bib` file:

```python
directory = './'
bib_filename = 'bibliography.bib'
```

## Has an item from a `.bib` file been cited in a `.tex` source file?

► [`is-it-cited.py`](is-it-cited.py)

Running this script on your `.bib` and `.tex` files will print a list of tags to bibliography items that have or have not been cited in your `.tex` source file. This will look something like this:

```
----------------------------------------
Citation not used: bray2005
Citation not used: buda2018
Citation not used: cox2008multidimensional
Citation not used: gicquel2000
Citation not used: gill2004improving
Citation not used: gri30
Citation not used: jolliffe2002
Citation not used: scikit-learn
Citation not used: szekely2007measuring
Citation not used: taylor1993multicomponent
Citation not used: tenenbaum2000global
Citation not used: van2008visualizing
Citation not used: yang2013empirical
Citation not used: yetter1991comprehensive
Citation not used: zhang2020large
      TOTAL NOT USED: 15
----------------------------------------
```

```
----------------------------------------
Citation used: isaac2015
Citation used: kambhatla1997dimension
      TOTAL USED: 2
----------------------------------------
```

The only thing you need to set in the script is the path to your `.bib` and `.tex` files:

```python
directory = './'
tex_filename = 'dissertation.tex'
bib_filename = 'bibliography.bib'
```

## Rename bibliography files to lower-case

► [`rename-bibliography-files.py`](rename-bibliography-files.py)

Running this script will get you from this:

![Screenshot](rename-before.png)

to this:

![Screenshot](rename-after.png)

The only thing you need to set in the script is the path to the directory where your downloaded literature items sit:

```python
path = './'
```

Note, that it will be ran recursively in all subdirectories of `path`.
