"""
@name: motif_analysis.py
@description:
Runs motif analysis

@author: 
@email: 
@date: 
"""

import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from inspect import getmembers,isfunction
from collections import namedtuple
import numpy as np

from igraph import Graph

from motifs import network_shuffle

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
    print(f"Input graph: {cfg['parameters']['input']}")
    G = Graph.Read_GraphML(cfg['parameters']['input']) 
    deg_test = np.array([G.degree(i) for i in range(G.vcount())])
    
    #In place shuffle of graph 
    print(f"Running shuffle method: {cfg['parameters']['shuffle_method']}")
    shuffle_method = getattr(network_shuffle, cfg['parameters']['shuffle_method'])
    shuffle_method(G,params=ARGS) 
    deg_shuffle = np.array([G.degree(i) for i in range(G.vcount())])
    
    #Check degree differences
    print(f"Max degree difference: {np.max(np.abs(deg_test - deg_shuffle))}")
