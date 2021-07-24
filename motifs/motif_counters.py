"""
@name: motif_counters.py
@description:
Callback functions for counting motifs

@author: Christopher Brittin
@email: "cabrittin"+ <at>+ "gmail"+ "."+ "com"
@date: 2019-12-05
"""

def aggregate_all(G,vertices,iso):
   #Stores all motifs
    tmp = [G.vs[v]['id'] for v in vertices]
    G.motif_store.append(tmp + [iso])

def count_ff(G,vertices,iso):
    """Counts FFWD motifs"""
    if iso == 7:
        tmp = [G.vs[v]['id'] for v in vertices]
        G.motif_store.append(tmp)

def count_fb(G,vertices,iso):
    """Counts FBK motifs"""
    if iso == 11:
        tmp = [G.vs[v]['id'] for v in vertices]
        G.motif_store.append(tmp)
        
def count_iso4(G,vertices,iso):
    """Counts isoclass 4 motifs"""
    if iso == 4:
        tmp = [G.vs[v]['id'] for v in vertices]
        G.motif_store.append(tmp)

