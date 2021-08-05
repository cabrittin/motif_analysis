"""
@name: random sample list generator.py
@description: Generates two sample lists of subgraphs (100 samples each). 
"with_common" only considers subgraphs with at least one of the nodes being a 
common node for ffls. "without_common" doesn't include any of these subgraphs.

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-08-04
"""

import csv
import random


with open("C:/Users/A N Other/motif_analysis/data/motifs/synapse4_reordered_motifs.csv", "r") as inp:
    reader = csv.reader(inp)
    subgraph_list = list(reader)
    
#print(subgraph_list)



i = 0
with_common = []
without_common = []
while i < len(subgraph_list):
     subgraph = subgraph_list[i]
     
     if ((subgraph[0].startswith("AVB") or subgraph[0].startswith("AIB") or subgraph[0].startswith("AIZ")) #or subgraph[0].startswith("RIM") or subgraph[0].startswith("AIA"))
     or (subgraph[1].startswith("AVB") or subgraph[1].startswith("AIB") or subgraph[1].startswith("AIZ")) #or subgraph[1].startswith("RIM") or subgraph[1].startswith("AIA"))
     or (subgraph[2].startswith("AVB") or subgraph[2].startswith("AIB") or subgraph[2].startswith("AIZ"))): #or subgraph[2].startswith("RIM") or subgraph[2].startswith("AIA"))):
             
         with_common.append(subgraph)
     else:
         without_common.append(subgraph)
             
     i = i + 1
    
print(len(with_common))
print(len(without_common))

j = 0
with_sample = []
without_sample = []
while j < 100:
    with_sample.append(random.choice(with_common))
    without_sample.append(random.choice(without_common))
    
    j = j + 1
    
with open("C:/Users/A N Other/motif_analysis/data_analysis/subgraph_sample_with_common", "w", newline="") as x:
    write = csv.writer(x)  
    write.writerows(with_sample)
    

with open("C:/Users/A N Other/motif_analysis/data_analysis/subgraph_sample_without_common", "w", newline="") as y:
    write = csv.writer(y)
    write.writerows(without_sample)



