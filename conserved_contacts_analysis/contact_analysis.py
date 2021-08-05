"""
@name: contact analysis.py
@description:
reads conserved_contacts and count_ff_motifs.csv, writing lists of edges. 
Then matches ffl edges with conserved_contact edges, determining whether 
ffls are accounted for by the synaptic contacts.

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-08-03
"""


import csv
import pandas as pd

df = pd.read_csv('conserved_contacts.csv')

#print(df["pre"].head())


# writing list of synaptic contacts
synaptic_contacts = []  
i = 0 
while i < len(df):
    if df.loc[i, "synapse_class"] != 0:
        synaptic_contacts.append([df.loc[i, "pre"], df.loc[i, "post"]])
        
    i = i + 1

#print(len(synaptic_contacts))


# writing lists of edges for each ffl (0-->1, 0-->2, 1-->2)
with open("C:/Users/A N Other/motif_analysis/data/motifs/ff_reordered_motifs.csv", "r") as inp:
    reader = csv.reader(inp)
    ffls = list(reader)
#print(ffls)

edge1 = [] # 0-->1
edge2 = [] # 0-->2
edge3 = [] # 1-->2
j = 0
while j < len(ffls):
    node = ffls[j]
    edge1.append([node[0], node[1]])
    edge2.append([node[0], node[2]])
    edge3.append([node[1], node[2]])
    j = j + 1

#print(len(edge1))

# 1. How many of the FFLs are accounted for by these synaptic contacts (synapse classes 1-3)?
ffl_present = []    
k = 0
while k < len(edge1):
    
    if ((edge1[k] in synaptic_contacts) and (edge2[k] in synaptic_contacts) and (edge3[k] in synaptic_contacts)):
        ffl_present.append(ffls[k])
    
    
    k = k + 1
    

print("Number of FFLs accounted for by the synaptic contacts: " + str(len(ffl_present)))

  
# 2. How many of the FFLs are established embryonically? i.e. how many of the FFL have all three edges in synapse class 3.

synaptic_contacts_class3 = []  
i = 0 
while i < len(df):
    if df.loc[i, "synapse_class"] == 3:
        synaptic_contacts_class3.append([df.loc[i, "pre"], df.loc[i, "post"]])
        
    i = i + 1

#print(len(synaptic_contacts_class3))

ffl_embryonic = []    
k = 0
while k < len(edge1):
    
    if ((edge1[k] in synaptic_contacts_class3) and (edge2[k] in synaptic_contacts_class3) and (edge3[k] in synaptic_contacts_class3)):
        ffl_embryonic.append(ffls[k])
    
    
    k = k + 1

print("Number of FFLs established embryonically: " + str(len(ffl_embryonic)))



# 3. How many of the FFLs are age dependent? i.e. how many FFL have edges from either synapse class 2 or 3.

synaptic_contacts_class23 = []  
i = 0 
while i < len(df):
    if (df.loc[i, "synapse_class"] == 2) or (df.loc[i, "synapse_class"] == 3):
        synaptic_contacts_class23.append([df.loc[i, "pre"], df.loc[i, "post"]])
        
    i = i + 1
#print(len(synaptic_contacts_class23))

ffl_age = []    
k = 0
while k < len(edge1):
    
    if ((edge1[k] in synaptic_contacts_class23) and (edge2[k] in synaptic_contacts_class23) and (edge3[k] in synaptic_contacts_class23)):
        ffl_age.append(ffls[k])
    
    
    k = k + 1

print("Number of age dependent FFLs: " + str(len(ffl_age)))


# 4. How many of the FFL have low reproducibility? i.e how many of the FFLs have at least 1 edge in synapse class 1.

synaptic_contacts_class1 = []  
i = 0 
while i < len(df):
    if (df.loc[i, "synapse_class"] == 1):
        synaptic_contacts_class1.append([df.loc[i, "pre"], df.loc[i, "post"]])
        
    i = i + 1
#print(len(synaptic_contacts_class1))


ffl_repro = []    
k = 0
while k < len(edge1):
    
    if (((edge1[k] in synaptic_contacts_class1) and (edge2[k] in synaptic_contacts_class23) and (edge3[k] in synaptic_contacts_class23))
    or ((edge1[k] in synaptic_contacts_class23) and (edge2[k] in synaptic_contacts_class1) and (edge3[k] in synaptic_contacts_class23))
    or ((edge1[k] in synaptic_contacts_class23) and (edge2[k] in synaptic_contacts_class23) and (edge3[k] in synaptic_contacts_class1))
    or ((edge1[k] in synaptic_contacts_class1) and (edge2[k] in synaptic_contacts_class1) and (edge3[k] in synaptic_contacts_class23))
    or ((edge1[k] in synaptic_contacts_class23) and (edge2[k] in synaptic_contacts_class1) and (edge3[k] in synaptic_contacts_class1))
    or ((edge1[k] in synaptic_contacts_class1) and (edge2[k] in synaptic_contacts_class23) and (edge3[k] in synaptic_contacts_class1))
    or ((edge1[k] in synaptic_contacts_class1) and (edge2[k] in synaptic_contacts_class1) and (edge3[k] in synaptic_contacts_class1))):
        ffl_repro.append(ffls[k])
  
    k = k + 1

print("Number of FFLs with low reproducibility: " + str(len(ffl_repro)))


  

             

                          
        
        
