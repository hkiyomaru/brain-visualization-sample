#Visualization of brain cells and their links


##Instruction

First, clone this repository.

```
$ git clone https://github.com/kiyomaro927/visualize_sample.git
```

I wrote all scripts written in Python2.7.0.

Some packages are required to execute these programs,

so you should install them.

```
$ pip install -r requirements.txt
```

If you use pyenv, this works well, too.

```
$ pyenv install anaconda-2.3.0
$ pyenv local anaconda-2.3.0
```

##Preparation of datasets

Download two datasets to the datasets directory.

1. [nature13186-s2.xlsx](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s2.xlsx)
2. [nature13186-s4.xlsx](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s4.xlsx)

And __save them as csv files__ in the same directory.

##Run

To show a graph with networkx,

```
$ python directed_graph.py
```

You should get a graph like this.

![networkx](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph1.png)

Fig1. This graph represents the relation between cells in the hippocampal formation.

##Gephi

[Gephi](https://gephi.org/) is one of the most famous visualization softwares.

If you have Gephi,

this provides a csv file which can use on it.

```
$ python extract_gephi_csv.py
```

The file created by this command will be saved in the gephi directory.

Open it with Gephi.

You can show a graph like this.

![gephi](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph2.png)

Fig2. What this graph represents is the same as the before graph.

This is the graph I tweaked.

![gephi_tweaked](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hf2hf.png)

Fig3. Sophisticatied graph


##Runtime options

When you execute

```
$ python directed_graph.py
```
or
```
$ python extract_gephi_csv.py
``` 

, you can use three options at run time.

####1. Change query

```
$ python extract_gephi_csv.py -query QUERY_STRING
```

By default, the query is "Hippocampal".

####2. Change query file path

```
$ python extract_gephi_csv.py -path QUERY_FILE_PATH
```

By default, the query is "datasets/nature13186-s2.csv".

####3. Select type of links between cells

```
$ python extract_gephi_csv.py -external
```

By defalt, the mode is "False".

This option provide all links beyond the brain region(which is given by your query).
