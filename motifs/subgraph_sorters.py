"""
@name: subgraph_sorters.py 

@description:
Module for sorting subgraphs

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-09
"""

import csv

def loop_through_subgraphs(func):
    def wrapper(*args,**kwargs):
        #Open grouping files and store as dict
        fptr,cfg = args
        with open(cfg['groupings'], mode ="r") as inp:
            subgraph_grp = {row[0]:row[1] for row in csv.reader(inp)}
        
        #Get isoclasses
        isoclasses = None
        if cfg['isoclasses'] not in ['ALL','all','All']:
            isoclasses = [int(n) for n in cfg['isoclasses'].split(',')]
        
        data = []
        for row in csv.reader(fptr):
            row[3] = int(row[3])
            if isoclasses and (row[3] not in isoclasses): continue
            _data = func(row[:3],subgraph_grp)
            if _data: data.append(row + _data)
        
        return data

    return wrapper

@loop_through_subgraphs
def unique_groups(*args,**kwargs):
    vertices,subgraph_grp = args
    try: 
        groups = [subgraph_grp[v] for v in vertices]
        unique_grps = len(set(groups))
        return groups + [unique_grps]
    except KeyError:
        print(f"KeyError for row: {vertices}")
        return None

@loop_through_subgraphs
def cell_position(*args, **kwargs):
    vertices, cell_class = args
    try: 
        groups = [cell_class[v] for v in vertices]
        return groups 
    except KeyError:
        print(f"KeyError for row: {vertices}")
        return None



""""
# Template function
@loop_through_subgraphs
def sorting_function(*args,**kwargs):
    # do stuff
"""

