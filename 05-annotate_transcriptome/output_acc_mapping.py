# output a table of gene, orig_acc, and new_acc for each sample

#%%

import cerberus

ca = cerberus.read('./annot_files/day0-1_samp_annot.h5')

#%%
df
#%%
import cerberus
import glob
import pandas as pd 
df = pd.DataFrame()
for f in glob.glob('./annot_files/*.h5'):
    ca = cerberus.read(f)
    df_new_sample = ca.t_map[['source', 'gene_name', 'original_transcript_id', 'transcript_id']]
    df = pd.concat([df, df_new_sample], axis=0)

#%%

df.to_csv('accession_mapping_all.tsv', sep='\t', index=False)
