"""
@name: isoclass sorting excel.py
@description: classifies each subgraph based on /mat csv files and 
tranfers info to excel spreadsheet, catagorised by isoclass.


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
outWorkbook = xlsxwriter.Workbook("out2.xlsx")
outSheet = outWorkbook.add_worksheet()

# write headers
# AC = anatomical classification 
# BL = brainmap layer
# SD - spatial domains
# no.s indicate corresponding node no.
outSheet.write("A1", "isoclass")
outSheet.write("B1", "AC1")
outSheet.write("C1", "AC2")
outSheet.write("D1", "AC3")
outSheet.write("E1", "BL1")
outSheet.write("F1", "BL2")
outSheet.write("G1", "BL3")
outSheet.write("H1", "SD1")
outSheet.write("I1", "SD2")
outSheet.write("J1", "SD3")

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

# subgraphs and tranferring data to spreadsheet
with open("C:/Users/A N Other/motif_analysis/data/motifs/aggregate_all_motifs.csv", mode ="r") as all_motifs:
    csv_reader = csv.reader(all_motifs)
    list_of_rows = list(csv_reader)
    i = 0
    while i < len(list_of_rows):
         list_of_elements = list_of_rows[i]
         
         isoclass = list_of_elements[3]
         subgraph = (list_of_elements[0], list_of_elements[1], list_of_elements[2], isoclass)
         
         outSheet.write((4*i)+1, 0, list_of_elements[3])
     
         a = list_of_elements[0]
         b = list_of_elements[1]
         c = list_of_elements[2]
             
         outSheet.write((4*i)+1, 1, anatom_dict.get(a))
         outSheet.write((4*i)+1, 2, anatom_dict.get(b))
         outSheet.write((4*i)+1, 3, anatom_dict.get(c))
         outSheet.write((4*i)+1, 4, brainmap_dict.get(a))
         outSheet.write((4*i)+1, 5, brainmap_dict.get(b))
         outSheet.write((4*i)+1, 6, brainmap_dict.get(c))
         outSheet.write((4*i)+1, 7, spatial_dict.get(a))
         outSheet.write((4*i)+1, 8, spatial_dict.get(b))
         outSheet.write((4*i)+1, 9, spatial_dict.get(c))
             
         
         i = i + 1
         
outWorkbook.close()         
         

         
         
       
        
            
        
     
             
            
             



   


    