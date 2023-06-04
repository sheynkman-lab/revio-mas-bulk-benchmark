# running cerberus commands to harmonize reference


# extract tss, tes, and ic information from pigeon output

# for day0
cerberus gtf_to_bed --mode tss --gtf day0_toy.gff -o day0_tss.bed --dist 50 --slack 50
cerberus gtf_to_bed --mode tes --gtf day0_toy.gff -o day0_tes.bed --dist 50 --slack 50
cerberus gtf_to_ics --gtf day0_toy.gff -o day0_ics.tsv

# for day5
cerberus gtf_to_bed --mode tss --gtf day5_toy.gff -o day5_tss.bed --dist 50 --slack 50
cerberus gtf_to_bed --mode tes --gtf day5_toy.gff -o day5_tes.bed --dist 50 --slack 50
cerberus gtf_to_ics --gtf day5_toy.gff -o day5_ics.tsv


# aggregate ends (tss and tes)
# need to make a config file that lists the files to aggregate and which runs will serve as a reference
cerberus agg_ends --mode tss --input pigeon_tss_beds.txt -o pigeon_tss_agg.bed
cerberus agg_ends --mode tes --input pigeon_tes_beds.txt -o pigeon_tes_agg.bed


# aggregate intron chains
cerberus agg_ics --input pigeon_ic_files.txt -o pigeon_ic_agg.tsv

# make cerberus reference
cerberus write_reference --tss pigeon_tss_agg.bed --tes pigeon_tes_agg.bed --ics pigeon_ic_agg.tsv -o pigeon.h5


### currently here

# make annotated transcriptome
cerberus annotate_transcriptome --gtf day0_toy.gff --h5 pigeon.h5 --source day0 -o day0_annot.h5

# make updated gtf with replaced accessions
cerberus replace_gtf_ids --h5 day0_annot.h5 --gtf day0_toy.gff --source day0 --collapse --update_ends -o day0_toy_harmonized_accs.gff