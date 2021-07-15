"""
@name: classifying subgraphs (no print).py
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
from matplotlib import pyplot as plt
import collections

CONFIG = 'configs/config.ini'

# node classification to dictionaries

with open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", mode ="r") as inp:
    anatom = csv.reader(inp)
    anatom_dict = {rows[0]:rows[1] for rows in anatom}
    
with open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", mode ="r") as inp:
    brainmap = csv.reader(inp)
    brainmap_dict = {rows[0]:rows[1] for rows in brainmap}

with open("C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv", mode ="r") as inp:
    spatial = csv.reader(inp)
    spatial_dict = {rows[0]:rows[1] for rows in spatial}

# looping through aggregate_all_motifs using dicts to classify
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_motifs.csv", mode ="r") as all_motifs:
    csv_reader = csv.reader(all_motifs)
    list_of_rows = list(csv_reader)
    i = 0
    while i < len(list_of_rows):
         list_of_elements = list_of_rows[i]
         
         
         subgraph = (list_of_elements[0], list_of_elements[1], list_of_elements[2])
         
     
         a = list_of_elements[0]
         node_1 = (anatom_dict.get(a), brainmap_dict.get(a), spatial_dict.get(a))
         

         b = list_of_elements[1]
         node_2 = (anatom_dict.get(b), brainmap_dict.get(b), spatial_dict.get(b))
         

         c = list_of_elements[2]
         node_3 = (anatom_dict.get(c), brainmap_dict.get(c), spatial_dict.get(c))
         
         anatom_subgraph = (anatom_dict.get(a), anatom_dict.get(b), anatom_dict.get(c))
         brainmap_subgraph = (brainmap_dict.get(a), brainmap_dict.get(b), brainmap_dict.get(c))
         spatial_subgraph = (spatial_dict.get(a), spatial_dict.get(b), spatial_dict.get(c))
         
         item = (subgraph, node_1, node_2, node_3)
         
       
        
     
         all_same = 0
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c):
             all_same += 1 
             print(all_same)
                    
        # if (spatial_dict.get(a) == "Lateral" and spatial_dict.get(b) == "Lateral" and spatial_dict.get(c) == "Lateral"):
         
          #   all_same_spat_dom += 1
          #   print(all_same_spat_dom)
             
#diff_spat_dom = 0
#two_thirds_same_spat_dom = 0
#all_same_spat_dom = 0

#for x in 
         
         i = i + 1
         

         
         
       
        
            
        
     
             
            
             



   


    