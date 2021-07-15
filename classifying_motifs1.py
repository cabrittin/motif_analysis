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


with open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", "r") as f:
   size_to_read = 100
   
   f_anatom = f.read(size_to_read)
   while len(f_anatom) > 0:
       print(f_anatom, end= "")
       f_anatom = f.read(size_to_read)

with open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", "r") as f:
   size_to_read = 100
   
   f_brainmap = f.read(size_to_read)
   while len(f_brainmap) > 0:
       print(f_brainmap, end= "")
       f_brainmap = f.read(size_to_read)
       
with open("C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv", "r") as f:
   size_to_read = 100
   
   f_spatial = f.read(size_to_read)
   while len(f_spatial) > 0:
       print(f_spatial, end= "")
       f_spatial = f.read(size_to_read)      

with open("C:/Users/A N Other/motif_analysis/data/motifs/aggregate_all_motifs.csv", "r") as f:
   size_to_read = 100
   
   f_motifs = f.read(size_to_read)
   while len(f_motifs) > 0:
       print(f_motifs, end= "")
       f_motifs = f.read(size_to_read) 

    