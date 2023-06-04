## aggregate ends (tss and tes)
## need to make a config file that lists the files to aggregate and which runs will serve as a reference
#cerberus agg_ends --mode tss --input tss_beds.txt -o tss_agg.bed
#cerberus agg_ends --mode tes --input tes_beds.txt -o tes_agg.bed


## aggregate intron chains
cerberus agg_ics --input ic_beds.txt -o ic_agg.tsv
#

