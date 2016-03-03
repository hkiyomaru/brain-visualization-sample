#Visualize sample


###Instruction

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

If you use pyenv,

this works well, too.

```
$ pyenv install anaconda-2.3.0
$ pyenv local anaconda-2.3.0
```

###Preparation of datasets

Download two datasets to the datasets directory.

1. [nature13186-s2.xlsx](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s2.xlsx)
2. [nature13186-s4.xlsx](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s4.xlsx)

And __save them as csv files__ in the same directory.

###Run

To show a graph with networkx,

```
$ python directed_graph.py
```

You should get a graph like this.

![networkx](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph1.png)

Fig1. This graph represents the relation between cells in the hippocampal formation and other cells.

###Gephi

[Gephi](https://gephi.org/) is one of the most famous visualization softwares.

If you have Gephi,

this provides a csv file which can use on it.

```
$ python extract_gephi_csv.py
```

Open the file created by this command with Gephi,

you can show a graph like this.

![gephi](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph2.png)

Fig2. What this graph represents is the same as the before graph.

And the part of the graph expanded is this.

![gephi_expanded](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph3.png)

Fig3. You can show a direction between cells. (Look ECT)
