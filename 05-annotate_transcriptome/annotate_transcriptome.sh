


# cerberus annotate_transcriptome --gtf ../01-prepare_pigeon_gffs/day0-1.gff --h5 ../04-make_reference/ec_diff_11samp.h5 --source day0-1 -o day0-1_samp_annot.h5

#!/bin/bash

input_dir="../01-prepare_pigeon_gffs"
output_dir="annot_files"

mkdir $output_dir

for file in "$input_dir"/day?-?.gff; do
    filename=$(basename "$file")
    sample_name="${filename%.gff}"
    output_file="${sample_name}_samp_annot.h5"

    # echo "cerberus annotate_transcriptome --gtf \"$file\" --h5 \"../4-make_reference/ec_diff_11samp.h5\" --source \"$sample_name\" -o \"$output_dir/$output_file\""

    cerberus annotate_transcriptome --gtf "$file" --h5 "../04-make_reference/ec_diff_11samp.h5" --source "$sample_name" -o "$output_dir/$output_file"
done