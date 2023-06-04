# visualize the reference

#%%
import cerberus

ca = cerberus.read('ec_diff_11samp_annot.h5')

#%%
ca.tss
#%%
ca.ic
#%%
ca.tes
#%%
ca.t_map
#%%
ca.t_map.source.unique() 