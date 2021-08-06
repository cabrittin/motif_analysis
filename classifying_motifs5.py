"""
@name: Documenting subgraph classification in Excel.py
@description:
Puts info from classifying_motifs4 / 6 into Excel spreadsheet

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
import xlsxwriter

# create excel
outWorkbook = xlsxwriter.Workbook("sorting_and_class_outputs/classifying_motifs_synapse4.xlsx")
outSheet = outWorkbook.add_worksheet()

# write headers
outSheet.write("A1", "Motifs")
outSheet.write("B1", "Anatomical Classification")
outSheet.write("C1", "Brainmap Layers")
outSheet.write("D1", "Spatial Domains")

# node classification 

with open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", mode ="r") as inp:
    anatom = csv.reader(inp)
    anatom_dict = {rows[0]:rows[1] for rows in anatom}
    
with open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", mode ="r") as inp:
    brainmap = csv.reader(inp)
    brainmap_dict = {rows[0]:rows[1] for rows in brainmap}

with open("C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv", mode ="r") as inp:
    spatial = csv.reader(inp)
    spatial_dict = {rows[0]:rows[1] for rows in spatial}

#storing to excel
with open("C:/Users/A N Other/motif_analysis/data/motifs/aggregate_all_motifs.csv", mode ="r") as all_motifs:
    csv_reader = csv.reader(all_motifs)
    list_of_rows = list(csv_reader)
    i = 0
    while i < len(list_of_rows):
         list_of_elements = list_of_rows[i]
         
         outSheet.write((4*i)+1, 0, list_of_elements[0])
         outSheet.write((4*i)+2, 0, list_of_elements[1])
         outSheet.write((4*i)+3, 0, list_of_elements[2])
         outSheet.write((4*i)+4, 0, list_of_elements[3])
             
   
         a = list_of_elements[0]
         
         outSheet.write((4*i)+1, 1, anatom_dict.get(a))
         outSheet.write((4*i)+1, 2, brainmap_dict.get(a))
         outSheet.write((4*i)+1, 3, spatial_dict.get(a))


         b = list_of_elements[1]
         
         outSheet.write((4*i)+2, 1, anatom_dict.get(b))
         outSheet.write((4*i)+2, 2, brainmap_dict.get(b))
         outSheet.write((4*i)+2, 3, spatial_dict.get(b))
         

         c = list_of_elements[2]
         
         outSheet.write((4*i)+3, 1, anatom_dict.get(c))
         outSheet.write((4*i)+3, 2, brainmap_dict.get(c))
         outSheet.write((4*i)+3, 3, spatial_dict.get(c))
        

         i = i + 1

outWorkbook.close()



   


    