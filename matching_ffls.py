"""
@name: matching ffls.py
@description:
reads through our count_ff_motifs csv file and determines how many of White et al.'s 
subgraphs occur in both

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-19
"""

import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
import csv
import pprint
from matplotlib import pyplot as plt
import collections
from collections import defaultdict
import hashlib
import numpy as np



# node classification to dictionaries
"""
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_motifs.csv", mode ="r") as inp:
    our_ff = csv.reader(inp)
    our_ff_dict = {}
    for row in our_ff:
        our_ff_dict[row[0]] = {"node2":row[1], "node3":row[2]}
#print(len(our_ff_dict))
#print(our_ff_dict) 
"""
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_motifs.csv") as our_ff:
    array = np.loadtxt(our_ff, delimiter=",")

print(array)
   

"""
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_white_only_chem_deg4_motifs.csv", mode ="r") as inp:
    white_ff = csv.reader(inp)
    white_ff_dict = {}
    for row in white_ff:
        white_ff_dict[row[0]] = {"node2":row[1], "node3":row[2]}
print(len(white_ff_dict))
"""
"""
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_motifs.csv", mode ="r") as inp:
    our_ff = csv.reader(inp)
   
    
    our_ff_dict = defaultdict(list)
    for row in our_ff:
        our_ff_dict[row[0]].append({"node2":row[1], "node3":row[2]})
print(len(our_ff_dict))
print(our_ff_dict)    
"""


"""
same_ff_dict = dict()
for key, value in our_ff_dict.items():
    if value in our_ff_dict.values():
        same_ff_dict[key] = value
print(same_ff_dict)
print(len(same_ff_dict))
 """     
 
"""
for (key, value) in our_ff_dict.items() & white_ff_dict.items():
    print('%s: %s, %s is present in both x and y' % (key, value, value))
"""
"""  
common_key_value_pairs  = our_ff_dict.items() & white_ff_dict.items()   
print("The common (key,value, value) pairs are :",common_key_value_pairs)
"""
# looping through aggregate_all_motifs using dicts to classify
with open("C:/Users/A N Other/motif_analysis/data/motifs/count_ff_motifs.csv", mode ="r") as all_motifs:
    csv_reader = csv.reader(all_motifs)
    list_of_rows = list(csv_reader)
    i = 0
    while i < len(list_of_rows):
         list_of_elements = list_of_rows[i]
         
         
         
       
        
         
         i = i + 1
         

         
         
       
        
            
        
     
             
            
             



   


    