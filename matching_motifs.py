"""
@name: matching ffls.py
@description:
reads through our count_ff_motifs csv file and determines how many of White et al.'s 
subgraphs occur in both

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-30
"""


import csv



with open("C:/Users/A N Other/motif_analysis/data/motifs/ff_reordered_motifs.csv", mode ="r") as inp:
    our_ff = csv.reader(inp)
    our_ff_list = []
    for row in our_ff:
        our_ff_list.append(row)

with open("C:/Users/A N Other/motif_analysis/data/motifs/white_deg4_iso7_reordered_motifs.csv", mode ="r") as inp:
    white_ff = csv.reader(inp)
    white_ff_list = []
    for row in white_ff:
        white_ff_list.append(row)  
        
matched_ff_list = [x for x in our_ff_list if x in white_ff_list]
print(len(matched_ff_list))


   
         
         
       
        
            
        
     
             
            
             



   


    