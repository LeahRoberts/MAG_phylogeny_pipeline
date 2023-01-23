"""
script that takes a directory and makes a fofn list
"""

import glob
import os


def make_fofn(genomes_dir, output_dir):
    files = glob.glob(genomes_dir)
    outputfile = output_dir + "fofn.txt"
    with open(outputfile, "a") as fout:
        for f in files:
            sample_name = os.path.splitext(os.path.basename(f))[0]
            fout.write("%s\%s\n" % (sample_name, f))


make_fofn(snakemake.input.genomes_dir, snakemake.input.output_dir)
