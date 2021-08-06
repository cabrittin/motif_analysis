"""
@name: graph randomizer.py
@description:
Loads input graph, shuffles edges (maintaining degree distribution), counts subgraphs
and outputs subgraph list to csv (currently #) OR outputs a dataframe with shuffle repeats,
their mean and standard deviation for each index.
Use this dataframe for further analysis (eg. calculating p-values)

NOTE: Slow for large number of repeats and often produces the following error:
    RuntimeError: fdopen() failed unexpectedly 
    
@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-08-05
"""

import argparse
from configparser import ConfigParser,ExtendedInterpolation
from collections import namedtuple
import csv
from igraph import Graph
import pandas as pd
import statistics as s
from motifs import network_shuffle
from motifs import motif_counters



CONFIG = 'configs/config.ini'
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
    ARGS = cfg[cfg['parameters']['shuffle_method']]
    ARGS = namedtuple("ARGS",ARGS.keys())(*ARGS.values())

    
    #Load input graph
    #print(f"Input graph: {cfg['parameters']['input']}")
    G = Graph.Read_GraphML(cfg['parameters']['input']) 
    
    all_repeats = []
    mean = []
    stdev = []
    pval = []
    i = 0
    while i < 100:
    
      motif_count = []
      zval = []
      x = 0
      while x < 20:
     
    
        #Shuffle graph G
        #print(f"Running shuffle method: {cfg['parameters']['shuffle_method']}")
        shuffle_method = getattr(network_shuffle, cfg['parameters']['shuffle_method'])
        shuffle_method(G,params=ARGS) 
    
    
        # Count motifs
        G.motif_store = []
    
  
        counter = getattr(motif_counters, cfg['parameters']['counter_callback'])
        G.motifs_randesu(size=3,callback=counter)  
    
    
        # Write output 
        #file = open(cfg['outputs']['motif_counts'], 'w+', newline ='')
       # with file:
           # write = csv.writer(file)
           # write.writerows(G.motif_store)
        #print("Written subgraph list of randomised graph to: " + cfg['outputs']['motif_counts'])
       
        motif_count.append(len(G.motif_store))
        
        x = x + 1
      
      all_repeats.append(motif_count)
      mean.append(s.mean(motif_count))
      stdev.append(s.stdev(motif_count))
      
      i = i + 1
    
    #print(all_repeats) 
    #print(mean)
    #print(stdev)
    
    repeats_df = pd.DataFrame(all_repeats, columns=["#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#15", "#16", "#17", "#18", "#19", "#20"])
    mean_df = pd.DataFrame(mean, columns=["Mean"])
    stdev_df = pd.DataFrame(stdev, columns=["Standard Deviation"])
    
    df1 = pd.merge(repeats_df, mean_df, left_index=True, right_index=True)
    df2 = pd.merge(df1, stdev_df,left_index=True, right_index=True) 
          
   
    df2.to_csv("C:/Users/A N Other/motif_analysis/data_analysis/shuffling_test_WHITE_ffl_counts.csv", index=True)
            
    print("Written to " + "C:/Users/A N Other/motif_analysis/data_analysis/shuffling_test_WHITE_ffl_counts.csv")
    
    