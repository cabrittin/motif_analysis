"""
@name: classifying subgraphs (print).py
@description:
reads /mat csv files to dictionary and loops through aggregate_all_motifs.csv
(from subgraph_4), classifying each.

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-07
"""

import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
import csv
import pprint

CONFIG = 'configs/config.ini'

# node classification 

with open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", mode ="r") as inp:
    anatom = csv.reader(inp)
    anatom_dict = {rows[0]:rows[1] for rows in anatom}
    
with open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", mode ="r") as inp:
    brainmap = csv.reader(inp)
    brainmap_dict = {rows[0]:rows[1] for rows in brainmap}

with open("C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv", mode ="r") as inp:
    spatial = csv.reader(inp)
    spatial_dict = {rows[0]:rows[1] for rows in spatial}


with open("C:/Users/A N Other/motif_analysis/data/motifs/aggregate_all_motifs.csv", mode ="r") as all_motifs:
    csv_reader = csv.reader(all_motifs)
    list_of_rows = list(csv_reader)
    i = 0
    while i < len(list_of_rows):
         list_of_elements = list_of_rows[i]
         
         print(list_of_elements[0], list_of_elements[1], list_of_elements[2], list_of_elements[3])
   
         a = list_of_elements[0]
         print(anatom_dict.get(a), brainmap_dict.get(a), spatial_dict.get(a))

         b = list_of_elements[1]
         print(anatom_dict.get(b), brainmap_dict.get(b), spatial_dict.get(b))

         c = list_of_elements[2]
         print(anatom_dict.get(c), brainmap_dict.get(c), spatial_dict.get(c))

         i = i + 1



   


    