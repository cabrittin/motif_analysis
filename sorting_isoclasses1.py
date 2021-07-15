"""
@name: Sorting specific isoclass motifs into subgroups based on their pattern of /mat
node characteristics. ===ALL_SAME==== 

@description:
Reads through the motif list for specific isoclass and categorises each 
motif based on parameters defined by the /mat classifications specified.
Tally is written to an excel spreadsheet, where the data can then be used to 
plot bar graphs (eg. can combine sets of data from different isoclasses to 
compare frequencies).

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-09
"""

import csv
import xlsxwriter

# create excel (indicate isoclass number next to "/mat category" (eg. spatial_domains2.xlsx) in workbook name)
outWorkbook = xlsxwriter.Workbook("all_same_spatial_domains7.xlsx")
outSheet = outWorkbook.add_worksheet()

# write headers
outSheet.write("A1", "All Anterior")
outSheet.write("B1", "All Avoidance")
outSheet.write("C1", "All Lateral")
outSheet.write("D1", "All Sublateral")
outSheet.write("E1", "All Taxis")
outSheet.write("F1", "All Unclassified")


# node classification to dictionaries using /mat csv files

with open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", mode ="r") as inp:
    anatom = csv.reader(inp)
    anatom_dict = {rows[0]:rows[1] for rows in anatom}
    
with open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", mode ="r") as inp:
    brainmap = csv.reader(inp)
    brainmap_dict = {rows[0]:rows[1] for rows in brainmap}

with open("C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv", mode ="r") as inp:
    spatial = csv.reader(inp)
    spatial_dict = {rows[0]:rows[1] for rows in spatial}


# looping through selected motifs csv file using above dicts to classify (need to count subgraph frequency of specific isoclass beforehand by adjusting motif_counters.py and config.ini)

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
         
# Defining parameters to consider for excel spreadsheet/ bar chart
         
         anterior = 0
         avoidance = 0
         lateral = 0
         sublateral = 0
         taxis = 0
         unclassified = 0
                 
# Note: can swap out for anatom_dict.get or brainmap_dict.get, or adjust to consider specific types (eg. lateral) 
        
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Anterior":
             anterior += 1
             
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Avoidance":
             avoidance += 1
         
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Lateral":
             lateral += 1  
        
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Sublateral":
             sublateral += 1
             
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Taxis":
             taxis += 1
             
         if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c) == "Unclassified":
             unclassified += 1
 
# Writing results to spreadsheet
            
         outSheet.write(i+1, 0, anterior)
         outSheet.write(i+1, 1, avoidance)
         outSheet.write(i+1, 2, lateral)
         outSheet.write(i+1, 3, sublateral)
         outSheet.write(i+1, 4, taxis)
         outSheet.write(i+1, 5, unclassified)
         
         
         i = i + 1
   
                        

outWorkbook.close()          
         
       
        
            
        
     
             
            
             



   


    