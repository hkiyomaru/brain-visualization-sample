#Visualize sample


###Instruction

First, clone this repo.

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

Download two datasets to datasets directory.

1. [nature13186-s2.xlsx](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s2.xlsx)
2. [nature13186-s4.xlsx](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s4.xlsx)

And save them as csv files in the same directory.

###Run

To show a graph with networkx,

```
$ python directed_graph.py
```

![networkx](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph1.png)

If you have Gephi,

this provides a csv file which can use on it.

```
$ python extract_gephi_csv.py
```


![networkx](https://raw.github.com/wiki/kiyomaro927/visualize_sample/images/hippocampal_connection_graph2.png)
