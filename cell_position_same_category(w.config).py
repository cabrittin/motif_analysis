"""
@name: classifying subgraphs in same spatial domain with cell position listed
@description:
reads position counter data and spatial domains csv to dictionary and loops through,
outputting a list of the nodes present in the specifed spatial domain with their 
corresponding position counter data. 

== adjust inputs as required in configs/phoebeconfig.ini ==

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-19
"""


import csv
import argparse
from configparser import ConfigParser,ExtendedInterpolation



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


# create dictionaries 

with open(cfg["parameters"]["subgraph_position_counter_data"], mode = "r") as inp:
    position_counter = csv.reader(inp)
    position_counter_dict = {}
    for row in position_counter:
        if len(row) == 4:
            
            position_counter_dict[row[0]] = [row[1],row[2],row[3]]
#print(position_counter_dict.get("ADA"))
 
with open(cfg["parameters"]["assortment_type"], mode ="r") as inp:
    spatial = csv.reader(inp)
    spatial_dict = {rows[0]:rows[1] for rows in spatial}
   
    
    
# loop through dictionaries and match nodes 
    
matched = set() 
for node, positions in position_counter_dict.items():
   for key, value in spatial_dict.items():
       for node in position_counter_dict:   
          if key.startswith(node) and value == cfg["parameters"]["category"]:
              if node not in matched:
                  print(node)
                  print(position_counter_dict.get(node))                  
                  matched.add(node)
                  
print(len(matched))
       


