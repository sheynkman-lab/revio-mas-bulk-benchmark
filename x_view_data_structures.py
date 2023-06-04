#%%
import cerberus
ca = cerberus.read('day0_annot.h5')
ca.tss

#%%
ca.tes

#%%
ca.ic

#%%
ca.t_map.source.unique() 

#%%
[x for x in dir(ca) if not x.startswith('_')]
#%%
ca.tes
#%%
ca.t_map

#%%
import pandas as pd

print(pd.__version__)