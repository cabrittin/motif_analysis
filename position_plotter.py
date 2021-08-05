"""
@name: Position Plotter.py
@description:
For selected isoclass list with selected constraint (eg.all in same spatial domain),
plots bar graph comparing each node's MOST COMMON position (not total count in that position)
in the subgraph.

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-30
"""
import argparse
from configparser import ConfigParser,ExtendedInterpolation
import csv
from matplotlib import pyplot as plt
import numpy as np

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
    
    # writing list of nodes and a list of frequency at each subgraph position (source, intermediate and sink)  
    with open(cfg["position_plotter"]["input"], "r") as inp:
        subgraphs = csv.reader(inp)
        node_positions = []
        position1 = []
        position2 = []
        position3 = []
        for row in subgraphs:
            node_positions.append(row)
            position1.append(int(row[1]))
            position2.append(int(row[2]))
            position3.append(int(row[3]))
           
    # writing lists of the most common position of each node  
    i = 0
    most_pos1 = []
    most_pos2 = []
    most_pos3 = []
    other = []
    while i < len(node_positions):
        list_of_elements = node_positions[i]
        
        if list_of_elements[1] > list_of_elements[2] and list_of_elements[1] > list_of_elements[3]:
            most_pos1.append(list_of_elements[0])
        
        elif list_of_elements[2] > list_of_elements[1] and list_of_elements[2] > list_of_elements[3]:
            most_pos2.append(list_of_elements[0])
            
        elif list_of_elements[3] > list_of_elements[1] and list_of_elements[3] > list_of_elements[2]:
            most_pos3.append(list_of_elements[0])
        
        else:
            other.append(list_of_elements[0])
            
            
        i = i + 1
    # writing lists of the number of times each position is most common (not total number of nodes in
    # this position!)
    sum_pos1 = len(most_pos1)
    sum_pos2 = len(most_pos2)
    sum_pos3 = len(most_pos3)
    sum_other = len(other)
    
    # plot to bar graph
    x_axis = ["Position 1", "Position 2", "Position 3"]
    y_axis = [sum_pos1, sum_pos2, sum_pos3]
        
    xpos = np.arange(len(x_axis))
    plt.xticks(xpos, x_axis)
    plt.ylabel("Frequency")
    plt.xlabel("Most Common Position In Subgraph")
    plt.title(cfg["position_plotter"]["graph_title"])
    
    for j in range(len(x_axis)):   
        plt.text(j, y_axis[j], y_axis[j], ha="center", va="bottom")
        
    plt.bar(xpos, y_axis, fc=cfg["position_plotter"]["colour"])
