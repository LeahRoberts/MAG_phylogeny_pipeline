# MAG_phylogeny_pipeline

Pipeline to generate phylogeny and Mandrake clusters from MAGs. 

Tested on:

* two species (B. uniformis, P. vulgatus)
* high quality MAGs (>90% complete, <1% contaminated)
* ~1000 MAGs at a time 


## Pre-processing MAGs:

No QC is done on the MAGs. You might consider species typing or basic QC before running this pipeline:

```
gtdbtk classify_wf --genome_dir fasta --extension fasta --out_dir pdorei_GTDB --cpus 10
```

## Dependencies:

* pp-sketchlib (via Poppunk)
* rapidNJ
* mandrake


**NOTE:** Conda is used to call different environments and dependencies (see Snakemake file).

## Input: 

* MAGs (fasta)


## Quick start: 

Update `config.yaml` to specify directory paths. 

Run snakemake (bash script for running on cluster using LSF):

```
bash submit_lsf.sh
```