import glob
import os

def make_file_of_filenames(directory, output_file):
    files = glob.glob(directory + "/*.fasta")
    for f in files:
        path, filename = os.path.split(f)
        sample, ext = os.path.splitext(filename)
        with open(output_file, "a") as fout:
            fout.write("%s\t%s\n" % (sample, f))

make_file_of_filenames(snakemake.input.MAGs, snakemake.output.fofn)