"""
@name: creating a tidy frame file.py
@description:


@author: Phoebe Cullen
@email: "cm20pic"+ <at>+ "leeds"+ "."+ "ac"+ "."+ "uk"
@date: 2021-07-28
"""

import argparse
from configparser import ConfigParser,ExtendedInterpolation
import csv
import pandas as pd

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

    #index
    index = list(range(1,int(cfg['cataloguing']['motif_#+1'])))
    index_df = pd.DataFrame(index, columns=["Index"])
    #print(index_df)
    
    
    #dataset
    dataset_type = cfg['cataloguing']['dataset']
    dataset = [[dataset_type] for x in range(1,3027)]
    dataset_df = pd.DataFrame(dataset, columns=["Dataset"])
    #print(dataset_df)
    
    
    with open(cfg['cataloguing']['input'], mode ='r') as subgraphs:
            subgraph_reader = csv.reader(subgraphs)
            
            #isoclass and cells
            
            isoclass = []
            cell1 = []
            cell2 = []
            cell3 = []
            
            for row in subgraph_reader:
                isoclass.append(row[3])
                cell1.append(row[0])
                cell2.append(row[1])
                cell3.append(row[2])
            
            
            isoclass_df = pd.DataFrame(isoclass, columns=["Isoclass"])
            cell1_df = pd.DataFrame(cell1, columns=["Cell 1"])
            cell2_df = pd.DataFrame(cell2, columns=["Cell 2"])
            cell3_df = pd.DataFrame(cell3, columns=["Cell 3"])
           
            #classes
            with open("mat/cell_class.csv", mode ="r") as inp:
                   class_reader = csv.reader(inp)
                   class_dict = {rows[0]:rows[1] for rows in class_reader}
                   
                   
                   class1 = []
                   class2 = []
                   class3 = []
                   i = 0 
                   while i < len(cell1):
                       class1.append(class_dict.get(cell1[i]))
                       class2.append(class_dict.get(cell2[i]))
                       class3.append(class_dict.get(cell3[i]))
                       
                       i = i + 1
                   
            class1_df = pd.DataFrame(class1, columns=["Class 1"])
            class2_df = pd.DataFrame(class2, columns=["Class 2"])
            class3_df = pd.DataFrame(class3, columns=["Class 3"])
                 
            
                       
            #spatial domains
            with open("mat/spatial_domains.csv", mode ="r") as inp:
                   spatial_domains_reader = csv.reader(inp)
                   spatial_domains_dict = {rows[0]:rows[1] for rows in spatial_domains_reader}
                   
                   spatdom1 = []
                   spatdom2 = []
                   spatdom3 = []
                   j = 0
                   while j < len(cell1):
                       spatdom1.append(spatial_domains_dict.get(cell1[j]))
                       spatdom2.append(spatial_domains_dict.get(cell2[j]))
                       spatdom3.append(spatial_domains_dict.get(cell3[j]))
                       
                       j = j + 1
                       
            spatdom1_df = pd.DataFrame(spatdom1, columns=["Spatial Domain 1"])
            spatdom2_df = pd.DataFrame(spatdom2, columns=["Spatial Domain 2"])
            spatdom3_df = pd.DataFrame(spatdom3, columns=["Spatial Domain 3"])
                  
                  
            #brainmap layer
            with open("mat/brainmap_layers.csv", mode ="r") as inp:
                brainmap_reader = csv.reader(inp)
                brainmap_dict = {rows[0]:rows[1] for rows in brainmap_reader}
                
                brainmap1 = []
                brainmap2 = []
                brainmap3 = []
                k = 0
                while k < len(cell1):
                    brainmap1.append(brainmap_dict.get(cell1[k]))
                    brainmap2.append(brainmap_dict.get(cell2[k]))               
                    brainmap3.append(brainmap_dict.get(cell3[k])) 
                    
                    k = k + 1
                
            brainmap1_df = pd.DataFrame(brainmap1, columns=["Brainmap Layer 1"])
            brainmap2_df = pd.DataFrame(brainmap2, columns=["Brainmap Layer 2"])               
            brainmap3_df = pd.DataFrame(brainmap3, columns=["Brainmap Layer 3"])              
            
             
            #anatomical classification
            with open("mat/anatomical_classification.csv", mode = "r") as inp:
                anatom_reader = csv.reader(inp)
                anatom_dict = {rows[0]:rows[1] for rows in anatom_reader}
                
                anatom1 = []
                anatom2 = []
                anatom3 = []
                l = 0
                while l < len(cell1):
                    anatom1.append(anatom_dict.get(cell1[l]))
                    anatom2.append(anatom_dict.get(cell2[l]))     
                    anatom3.append(anatom_dict.get(cell3[l]))   
                    
                    l = l + 1
            
            anatom1_df = pd.DataFrame(anatom1, columns=["Anatomical Class 1"])
            anatom2_df = pd.DataFrame(anatom2, columns=["Anatomical Class 2"])
            anatom3_df = pd.DataFrame(anatom3, columns=["Anatomical Class 3"])
            
            #merging dataframes
            df1 = pd.merge(index_df, dataset_df, left_index=True, right_index=True)
            df2 = pd.merge(isoclass_df, cell1_df, left_index=True, right_index=True)
            df3 = pd.merge(cell2_df, cell3_df, left_index=True, right_index=True)
            df4 = pd.merge(class1_df, class2_df, left_index=True, right_index=True)
            df5 = pd.merge(class3_df, spatdom1_df, left_index=True, right_index=True)
            df6 = pd.merge(spatdom2_df, spatdom3_df, left_index=True, right_index=True)
            df7 = pd.merge(brainmap1_df, brainmap2_df, left_index=True, right_index=True)
            df8 = pd.merge(brainmap3_df, anatom1_df, left_index=True, right_index=True)
            df9 = pd.merge(anatom2_df, anatom3_df, left_index=True, right_index=True)
            
            df10 = pd.merge(df1, df2, left_index=True, right_index=True)
            df11 = pd.merge(df3, df4, left_index=True, right_index=True)
            df12 = pd.merge(df5, df6, left_index=True, right_index=True)
            df13 = pd.merge(df7, df8, left_index=True, right_index=True)
            
            df14 = pd.merge(df10, df11, left_index=True, right_index=True)
            df15 = pd.merge(df12, df13, left_index=True, right_index=True)
            
            df16 = pd.merge(df14, df15, left_index=True, right_index=True)
            
            merged_df = pd.merge(df16, df9, left_index=True, right_index=True)
            
            
            #write csv
            merged_df.to_csv(cfg['cataloguing']['output'], index=False)
            
            print("Written to " + cfg['cataloguing']['output'])