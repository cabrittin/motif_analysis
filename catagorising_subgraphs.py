"""
@name: categorising_subgraphs.py
@description: Sorting subgraph lists based on mat categories.
Can be used for preprocessing before inputting subgraph list into
position counter function.


@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-30
"""

import argparse
from configparser import ConfigParser,ExtendedInterpolation
import csv


CONFIG = 'configs/phoebeconfig.ini'
if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c','--config',
                        dest = 'config',
                        action = 'store',
                        default = CONFIG,
                        required = False,
                        help = 'Config file')

 
    params = parser.parse_args()
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(params.config)

    #writing catagories to dictionaries
    with open("C:/Users/A N Other/motif_analysis/mat/anatomical_classification.csv", mode ="r") as inp:
        anatom = csv.reader(inp)
        anatom_dict = {rows[0]:rows[1] for rows in anatom}
        
    with open("C:/Users/A N Other/motif_analysis/mat/brainmap_layers.csv", mode ="r") as inp:
        brainmap = csv.reader(inp)
        brainmap_dict = {rows[0]:rows[1] for rows in brainmap}
    
    with open("C:/Users/A N Other/motif_analysis/mat/spatial_domains.csv", mode ="r") as inp:
        spatial = csv.reader(inp)
        spatial_dict = {rows[0]:rows[1] for rows in spatial}
        
    #input file to list 
    with open(cfg["catagorising_subgraphs"]["input"], mode ="r") as inp:
        csv_reader = csv.reader(inp)
        motif_list = list(csv_reader) 
        
        i = 0
           
        subgraph_list = []
        node_1_list = []
        node_2_list = []
        node_3_list = []
        item_list = []
        anatom_subgraph_list = []
        brainmap_subgraph_list = []
        spatial_subgraph_list = []
        all_same = []
        
        # looping through each (including all categories in case the code is adapted)
        while i < len(motif_list):
             node_list = motif_list[i]
             
            
             subgraph = (node_list[0], node_list[1], node_list[2], node_list[3])
            
         
             a = node_list[0]
             node_1 = (anatom_dict.get(a), brainmap_dict.get(a), spatial_dict.get(a))
             
    
             b = node_list[1]
             node_2 = (anatom_dict.get(b), brainmap_dict.get(b), spatial_dict.get(b))
            
    
             c = node_list[2]
             node_3 = (anatom_dict.get(c), brainmap_dict.get(c), spatial_dict.get(c))
             
             anatom_subgraph = (anatom_dict.get(a), anatom_dict.get(b), anatom_dict.get(c))
             brainmap_subgraph = (brainmap_dict.get(a), brainmap_dict.get(b), brainmap_dict.get(c))
             spatial_subgraph = (spatial_dict.get(a), spatial_dict.get(b), spatial_dict.get(c))
             
             
             item = (subgraph, node_1, node_2, node_3)
             
             subgraph_list.append(subgraph)
             node_1_list.append(node_1)
             node_2_list.append(node_2)
             node_3_list.append(node_3)
             anatom_subgraph_list.append(anatom_subgraph)
             brainmap_subgraph_list.append(brainmap_subgraph)
             spatial_subgraph_list.append(spatial_subgraph)
             item_list.append(item)
             # choice of constraint
             if spatial_dict.get(a) == spatial_dict.get(b) == spatial_dict.get(c):
                all_same.append(subgraph)
                       
             i = i + 1
             
    print(len(all_same))
    #writing output to csv 
    with open(cfg["catagorising_subgraphs"]["output"], 'w', newline="") as f:
        write = csv.writer(f)   
        write.writerows(all_same)
    
             
    print("Written to " + cfg["catagorising_subgraphs"]["output"])
        
    
    