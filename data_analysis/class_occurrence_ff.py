"""
@name: FFL Count.py
@description:
Using "ffl_common_occurrence" as a guide to pick the cells that account for the majority
of the FFLs, iterate through list of all 3-node subgraphs and write any containing
at least one of these common nodes to a list. Outputs csv where it is stated whether
or not subgraph is a ffl (in binary, 1=ffl).

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-08-02
"""
import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
import csv
import pprint
from matplotlib import pyplot as plt
import collections
import pandas as pd


with open("C:/Users/A N Other/motif_analysis/data/motifs/synapse4_reordered_motifs.csv", "r") as inp:
    reader = csv.reader(inp)
    subgraph_list = list(reader)

#writing list of subgraphs in selected isoclass containing at least of the chosen class nodes
i = 0
common = []
while i < len(subgraph_list):
     subgraph = subgraph_list[i]
     
     if ((subgraph[0].startswith("AVB") or subgraph[0].startswith("AIB") or subgraph[0].startswith("AIZ")) #or subgraph[0].startswith("RIM") or subgraph[0].startswith("AIA"))
     or (subgraph[1].startswith("AVB") or subgraph[1].startswith("AIB") or subgraph[1].startswith("AIZ")) #or subgraph[1].startswith("RIM") or subgraph[1].startswith("AIA"))
     or (subgraph[2].startswith("AVB") or subgraph[2].startswith("AIB") or subgraph[2].startswith("AIZ"))): #or subgraph[2].startswith("RIM") or subgraph[2].startswith("AIA"))):
             
             common.append(subgraph)
             
     i = i + 1
     
print(len(common))

j = 0
common_and_ff = []
while j < len(common):
    subgraph = common[j]
    if subgraph[3] == "7":
        
        common_and_ff.append(subgraph)
        
    j = j + 1
    
print(len(common_and_ff))


k = 0
ffl_binary = []
while k < len(common):
    subgraph = common[k]
    if subgraph[3] == "7":
        
        ffl_binary.append("1")
    else:
        ffl_binary.append("0")
        
    k = k + 1

#print(ffl_binary)

ffl_binary_df = pd.DataFrame(ffl_binary, columns=["FFL?"])
print(ffl_binary_df)

ffl_binary_df.to_csv("C:/Users/A N Other/motif_analysis/data_analysis/ffl_common_occurrence.csv", index="True")

             
