"""
@name: plot_sorters.py 

@description:
Module for ploting results from subgraph sorters

@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-09
"""

from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

def unique_groups(func):
    def wrapper(data):
        df = DataFrame(
                    data,
                    columns=['Cell1','Cell2','Cell3','Isoclass',
                            'Group1','Group2','Group3','Unique groups']
                    )
        
        
        fig,ax = plt.subplots(1,2,figsize=(8,4))
        sns.countplot(ax=ax[0],x='Unique groups',hue='Isoclass',data=df)
        #Normalized counts
        y = 'Unique groups'
        x = 'Isoclass'
        df2 = df.groupby(x)[y].value_counts(normalize=True).rename('percent').reset_index()
        sns.barplot(ax=ax[1],x='Unique groups',y='percent',hue='Isoclass',data=df2)
        
        func([ax,df,df2])
        plt.show()
        
    return wrapper

@unique_groups
def unique_domains(plots):
    ax,df,df2 = plots
    for _ax in ax: _ax.set_xlabel('# spatial domains')
            
@unique_groups
def unique_layers(plots):
    ax,df,df2 = plots
    for _ax in ax: _ax.set_xlabel('# brain map layers')
 
