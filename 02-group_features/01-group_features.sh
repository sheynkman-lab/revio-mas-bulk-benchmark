# run grouping for tss and tes

types=("tss" "tes")

for type in "${types[@]}"; do
	mkdir "$type"
done

for file in ../01-prepare_pigeon_gffs/day?-?.gff; do
	sample=$(basename "$file" .gff)
	for type in "${types[@]}"; do
		cerberus gtf_to_bed --mode $type --gtf $file -o ${type}/${sample}_${type}.bed --dist 50 --slack 50
	done
done

mkdir ics

for file in ../01-prepare_pigeon_gffs/day?-?.gff; do
	sample=$(basename "$file" .gff)
	cerberus gtf_to_ics --gtf ${file} -o ics/${sample}_ics.tsv
done