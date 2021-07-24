# -*- coding: utf-8 -*-
"""
@description:
Correcting FANMOD ordering issue and reordering based on difference between input and output degree.
Input = old count_motif outputs
Output = writes new subgraph lists

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-23
"""


import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
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
    
    # Read graph input
    G = Graph.Read_GraphML(cfg['reordering_graphs']['input'])
    G.motif_store = []
    
    with open(cfg["reordering_graphs"]["subgraph_list"], mode ="r") as inp:
      all_subgraphs = csv.reader(inp)
      subgraph_list = []
      for subgraph in all_subgraphs:
        subgraph_list.append(subgraph)
      #print(subgraph_list)
  

    
    #Count degree difference (deg) of each node from input graph (G) and writes dictionary of node:deg
    deg = []
    vertex_deg_dict = {}
    i = 0
    while i < G.vcount():
        
        deg = G.vs[i].outdegree() - G.vs[i].indegree()
        
        vertex_deg_dict[G.vs[i]["id"]] = deg
        
        i = i + 1
     
    sort_dict = dict(sorted(vertex_deg_dict.items(), key=lambda x:x[1], reverse=True))
   
    #print(sort_dict)
    #test_list = [["A", "C", "B"]]
    
    
    file = open(cfg['outputs']['sorted_motifs'], 'w+', newline ='')
    with file:
           write = csv.writer(file)
           
           j = 0
           while j < len(subgraph_list):
        
                res = sorted(subgraph_list[j], key = lambda ele: sort_dict[ele], reverse=True)
                #print(res)
                write.writerow(res)
                j = j+1
       
    print(f"Wrote reordered motifs to: {cfg['outputs']['sorted_motifs']}")
    
 
    
    
   
   
                
    