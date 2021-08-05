"""
@name: .py
@description:


@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-08-04
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import csv
import random
from collections import Counter
# how many samples in total per x value (e.g. 100)
sample_size = 100

with open("C:/Users/A N Other/motif_analysis/data_analysis/subgraph_sample_with_common1", "r") as inp:
    reader = csv.reader(inp)
    with_common = list(reader)
    
with open("C:/Users/A N Other/motif_analysis/data_analysis/subgraph_sample_without_common1", "r") as inp:
    reader = csv.reader(inp)
    without_common = list(reader)

subgraph_sample = []
i = 0
while i < (sample_size):
   subgraph_sample.append(random.sample(with_common,k = i) + random.sample(without_common, k = (sample_size - i)))
   
   i = i + 1

#print(subgraph_sample)

isoclass = []
j = 0
while j < (sample_size):
    k = 0
    while k < (sample_size):
        
        isoclass.append(subgraph_sample[j][k][3])
        
        k = k + 1
    j = j + 1

#print(isoclass)

group_isos = []
for pos in range(0, len(isoclass), sample_size):
    group_isos.append(isoclass[pos:pos+sample_size])
print(len(group_isos))

ffl_count = []
m = 0
while m < len(group_isos):
    
    ffl_count.append(group_isos[m].count("7"))
    
    m = m + 1

#print(ffl_count)

ffl_percentage = []
n = 0
while n < len(ffl_count):
    
    ffl_percentage.append(int(ffl_count[n]) / 100)
    
    n = n + 1

#print(ffl_percentage)

# graph plot

x = range(100)
y = ffl_percentage

plt.scatter(x,y)
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.title('Comparing Relationship Between Proportion of Common Node Graphs and Proportion of FFL Subgraphs')
plt.xlabel('# Subgraphs With At Least 1 of The FFL Common Nodes (/100)')
plt.ylabel('% Of Subgraphs That Are FFL')
plt.show()
    
