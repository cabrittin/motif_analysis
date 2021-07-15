"""
@name: count_ff_fb_motifs.py
@description:


@author: Christopher Brittin
@email: "cabrittin"+ <at>+ "gmail"+ "."+ "com"
@date: 2019-12-05
"""

import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
import csv
import pprint

CONFIG = 'configs/config.ini'


anatomical_class = open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", "r")
d = {}
for line in anatomical_class:
    x = line.split(",")
    node = x[0]
    classi = x[1]
    d[node] = classi
    print(line)
anatomical_class.close()

brainmap = open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", "r")
d = {}
for line in brainmap:
    x = line.split(",")
    node = x[0]
    layer = x[1]
    d[node] = layer
    print(line)
brainmap.close()
        


    