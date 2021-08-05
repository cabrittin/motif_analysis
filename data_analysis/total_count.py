"""
@name: finding most common nodes.py
@description:
Uses output from position count to count overall class occurance. Outputs csv 
with class, frequency in isoclass, percent frequency in isoclass (out of total classes
in that isoclass)

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

with open("C:/Users/A N Other/motif_analysis/data/position_outputs/pos_counter_reordered_iso7_ALL.csv", mode="r") as inp:
    reader = csv.reader(inp)
    pos_list = list(reader)



total_count = []
nodes = []
i = 0
while i < len(pos_list):
    element_list = pos_list[i]
    nodes.append(element_list[0])
    i = i + 1
    
overall = []   
for row in pos_list:
    overall.append(int(row[1]) + int(row[2]) + int(row[3]))

    

summ = sum(overall)


percent = []
k = 0
while k < len(overall):
    percent.append(overall[k]/summ)
    k = k + 1
    

nodes_df = pd.DataFrame(nodes, columns=["Class"])
overall_df = pd.DataFrame(overall, columns=["Frequency"])
percent_df = pd.DataFrame(percent, columns=["Percent of Total"])

df1 = pd.merge(nodes_df, overall_df, left_index=True, right_index=True)

df2 = pd.merge(df1, percent_df, left_index=True, right_index=True) 

df2.sort_values(by=["Frequency"], inplace=True, ascending=False)
df2 = df2.reset_index(drop=True)



df2.to_csv("C:/Users/A N Other/motif_analysis/data_analysis/ff_class_count.csv", index=True)






















    