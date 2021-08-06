"""
@name: p-value calculator  NOT COMPLETE

@description: Uses output from graph_randomizer.py and computes p-values


@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-08-06
"""

import argparse
from configparser import ConfigParser,ExtendedInterpolation
from collections import namedtuple
import csv
from igraph import Graph
import numpy as np
import pandas as pd
import statistics as s
from motifs import network_shuffle
from motifs import motif_counters
from motifs import mht



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
    
    
    df = pd.read_csv('C:/Users/A N Other/motif_analysis/data_analysis/shuffling_test_ffl_counts.csv')
    
    #print(df1.loc[0])
    
    
   
    pcalc = getattr(mht, "pval_norm_one_sided")
    pvals = pcalc(df)
    
    
   
  
    
       