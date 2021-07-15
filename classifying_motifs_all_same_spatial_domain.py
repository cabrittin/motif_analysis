"""
@name: classifying subgraphs (spatial domain = all same).py
@description:
reads /mat csv files to dictionary and loops through count_ff_motifs.csv
(from subgraph_4), classifying each.

== used to find out if the ffls all in the chosen spatial domain are dominated
by certain nodes. == 

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-14
"""

import csv


 

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
         

         item = (subgraph, node_1, node_2, node_3)
         
         
         
            
             
         #with open("class_outputs/taxis_only_ff_motifs.csv", "w", newline="") as f:
             #writer = csv.writer(f)
             #if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Taxis":
                 #writer.writerow(subgraph)
                 #print(subgraph)
        
        # if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c):    
         if brainmap_dict.get(a) == brainmap_dict.get(b) == brainmap_dict.get(c):
               print(item)  
             
         i = i + 1
         

         
         
       
        
            
        
     
             
            
             



   


    