"""
@name: Analysing Isoclass 7 (FF).py
@description:
Use to set filter ffls depending on chosen constraints (ie. all same spatial domain)

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-08
"""

import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
import csv
import pprint
import numpy as np

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
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_motifs.csv", mode ="r") as ff_motifs:
    csv_reader = csv.reader(ff_motifs)
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
         
         item = (subgraph, node_1, node_2, node_3) 
         
         count = 0
         
         print("(" + anatom_dict.get(a),anatom_dict.get(b),anatom_dict.get(c) + "), ")
         
         if spatial_dict.get(a) == "Lateral" and spatial_dict.get(b) == "Taxis" and spatial_dict.get(c) == "Taxis":
            count = count + 1
            #(count)
         
         i = i + 1
        
       

         
         
       
        
            
        
     
             
            
             



   


    