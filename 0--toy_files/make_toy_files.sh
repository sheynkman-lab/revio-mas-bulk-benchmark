# note - ran the code block below before restructuring directory
# make a toy gff for day0 and day5 to process in cerberus
# here, processing these files:
#    GS_230501_Day0-1.lima.0--0.lima.IsoSeqX_bc10_5p--IsoSeqX_3p.collapsed_transcripts.sorted
#    GS_230501_Day5-1.lima.0--0.lima.IsoSeqX_bc06_5p--IsoSeqX_3p.collapsed_transcripts.sorted.gff
grep -v SIRV *Day0* | head -n 10012 > day0_toy.gff
grep -v SIRV *Day5* | head -n 9999 > day5_toy.gff

