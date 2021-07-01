""""
random.py

Modules for generating randomized networks.

Functions
---------
edge_switch(G,iters=1000)
  Randomly switch edges in graph G (igraph). Do iters random switches.
  Preserves in degree and out degree.

mp_edge_switch(G,proFunc,njobs=2,sub_iters=500,es_iters=1000):
  Do random edge switches in parallel

_mp_edge_switch(G,procFunc,output,sub_iters,es_iters):
  Target function for mp_edge_switch.


"""
from random import randint
from random import sample

def edge_switch(G,iters=1000,params=None):
    """
    Randomly switch edges in graph G (igraph). Do iters random switches.
    Preserves in degree and out degree.

    Parameters
    ----------
    G : iGraph
     Graph in which edges will be randomly switched
    iters : int (default 1000)
     Number of edge switches to perform 
    params: namedtuple (default None)
     Passes parameters using nametuple

    """
    
    if params:
        iters = int(params.iters)

    N = G.ecount() - 2
    idx = 0
    while idx < iters:
        i = randint(0,N)
        j = i
        while j == i: j = randint(0,N)
        ei = G.es[i]
        ej = G.es[j]
        u1 = ei.source
        v1 = ei.target
        u2 = ej.source
        v2 = ej.target
        iattr = ei.attributes()
        jattr = ej.attributes()
        cond1 = len(set([u1,v1,u2,v2])) == 4
        cond2 = not G.are_connected(u1,v2) 
        cond3 = not G.are_connected(u2,v1) 
        if cond1 and cond2 and cond3: 
            G.delete_edges([i,j])
            G.add_edge(u1,v2,**iattr)
            G.add_edge(u2,v1,**jattr)
            idx += 1
