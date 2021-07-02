"""
@name: count_ff_fb_motifs.py
@description:


@author: Christopher Brittin
@email: "cabrittin"+ <at>+ "gmail"+ "."+ "com"
@date: 2019-12-05
"""

import os
import argparse
from configparser import ConfigParser,ExtendedInterpolation
from igraph import Graph
import csv

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
    
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(params.config)
    
    # Read graph input
    G = Graph.Read_GraphML(cfg['parameters']['input'])
    G.motif_store = []
    
    # Count motifs
    counter = getattr(motif_counters, cfg['parameters']['counter_callback'])
    G.motifs_randesu(size=3,callback=counter)    
    
    # Write output 
    file = open(cfg['outputs']['motif_counts'], 'w+', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(G.motif_store)

    print(f"Wrote motifs to: {cfg['outputs']['motif_counts']}")


