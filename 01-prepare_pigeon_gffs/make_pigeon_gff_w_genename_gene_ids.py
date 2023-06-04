#%%

import csv
import os


# example of the input files including gff and classifications table
# GS_230501_Day0-1.lima.0--0.lima.IsoSeqX_bc10_5p--IsoSeqX_3p.collapsed_transcripts.sorted.filtered_lite.gff
# GS_230501_Day0-1.lima.0--0.lima.IsoSeqX_bc10_5p--IsoSeqX_3p.collapsed_transcripts.sorted.gff
# GS_230501_Day0-1.lima.0--0.lima.IsoSeqX_bc10_5p--IsoSeqX_3p.collapsed_transcripts_classification.filtered_lite_classification.txt
# GS_230501_Day0-1.lima.0--0.lima.IsoSeqX_bc10_5p--IsoSeqX_3p.collapsed_transcripts_classification.txt
# GS_230501_Day0-2.lima.0--0.lima.IsoSeqX_bc11_5p--IsoSeqX_3p.collapsed_transcripts.sorted.filtered_lite.gff
# GS_230501_Day0-2.lima.0--0.lima.IsoSeqX_bc11_5p--IsoSeqX_3p.collapsed_transcripts.sorted.gff
# GS_230501_Day0-2.lima.0--0.lima.IsoSeqX_bc11_5p--IsoSeqX_3p.collapsed_transcripts_classification.filtered_lite_classification.txt

dir = '../00-input_data/'

for filename in sorted(os.listdir(dir)):
    if filename.endswith('collapsed_transcripts_classification.txt'):

        sample = 'day' + str(filename.split('_Day')[1].split('.')[0])

        # path to the pigeon gff file
        gff_file_path = os.path.join(dir, filename.replace('_classification.txt', '.sorted.gff'))

        # path to the isoform classifications file
        lookup_table_file_path = os.path.join(dir, filename)

        # Create a dictionary to store the gene_id to associated_gene mapping
        lookup_table = {}

        # Read the lookup table file
        with open(lookup_table_file_path, 'r') as lookup_file:
            reader = csv.DictReader(lookup_file, delimiter='\t')
            for row in reader:
                gene_id = 'PB.' + row['isoform'].split('.')[1]
                associated_gene = row['associated_gene']
                lookup_table[gene_id] = associated_gene

        # Generate the new versions of the GFF files
        with open(gff_file_path, 'r') as gff_file:
            lines = gff_file.readlines()

            # Initialize lists to store the updated GFF lines
            updated_lines_main = []
            updated_lines_novel = []

            # Iterate over the lines and replace gene_id with associated_gene
            for line in lines:
                if line.startswith('#'):
                    updated_lines_main.append(line)
                    updated_lines_novel.append(line)
                else:
                    parts = line.split('\t')
                    attributes = parts[8].split(';')
                    gene_id = attributes[0].strip().split('"')[1]
                    if gene_id in lookup_table:
                        associated_gene = lookup_table[gene_id]
                        attributes[0] = f'gene_id "{associated_gene}"'
                        if associated_gene.startswith('novel'):
                            updated_lines_novel.append('\t'.join(parts[:8]) + '\t' + ';'.join(attributes))
                        else:
                            updated_lines_main.append('\t'.join(parts[:8]) + '\t' + ';'.join(attributes))
                    else:
                        print(f"Warning PB missing in lookup table. {gene_id}")

            # Write the updated GFF lines to new files
            updated_gff_file_path_main = f'{sample}.gff'
            updated_gff_file_path_novel = f'{sample}_no_gene_matches.gff'

            with open(updated_gff_file_path_main, 'w') as updated_gff_file_main:
                updated_gff_file_main.writelines(updated_lines_main)

            with open(updated_gff_file_path_novel, 'w') as updated_gff_file_novel:
                updated_gff_file_novel.writelines(updated_lines_novel)


