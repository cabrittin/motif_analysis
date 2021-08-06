"""
@name: sort_subgraphs.py

@author: Christopher Brittin
@email: "cabrittin"+ <at>+ "gmail"+ "."+ "com"
@date: 
"""


import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
import csv

from motifs import subgraph_sorters
from motifs import plot_sorters

CONFIG = 'configs/config.ini'


def run(cfg_path):
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(cfg_path)
    
    #Loop through subgraph file
    sorter = getattr(subgraph_sorters, cfg['sort_subgraphs']['subgraph_sorter'])
    with open(cfg['sort_subgraphs']['subgraph_file'],mode="r") as fptr:
        data = sorter(fptr,cfg['sort_subgraphs'])    
    
    #Plot results
    plotter = getattr(plot_sorters, cfg['sort_subgraphs']['plot_sorter'])
    plotter(data)
 
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
    run(params.config)
    
