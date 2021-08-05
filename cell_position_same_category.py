"""
@name: classifying subgraphs in same spatial domain with cell position listed
@description:
reads position counter data and spatial domains csv to dictionary and loops through,
outputting a list of the nodes present in the specifed spatial domain with their 
corresponding position counter data. 

adjust input position counter data and spatial domain as required

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-19
"""


import csv
import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph


#Parameters

subgraph_position_counter_data = "C:/Users/A N Other/motif_analysis/data/position_outputs/pos_counter_reordered_iso7_ALL.csv"
assortment_type = "C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv" 
#assortment_type = "C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv"
#assortment_type = "C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv"
category = "Taxis"


# create dictionaries 

with open(subgraph_position_counter_data, mode = "r") as inp:
    position_counter = csv.reader(inp)
    position_counter_dict = {}
    for row in position_counter:
        if len(row) == 4:
            
            position_counter_dict[row[0]] = [row[1],row[2],row[3]]
#print(position_counter_dict.get("ADA"))
 
with open(assortment_type, mode ="r") as inp:
    spatial = csv.reader(inp)
    spatial_dict = {rows[0]:rows[1] for rows in spatial}
    
    
# loop through dictionaries and match nodes 
    
matched = set() 
for node, positions in position_counter_dict.items():
   for key, value in spatial_dict.items():
       for node in position_counter_dict:   
          if key.startswith(node) and value == category:
              if node not in matched:
                  print(node)
                  print(position_counter_dict.get(node))                  
                  matched.add(node)
print(len(matched))
       


