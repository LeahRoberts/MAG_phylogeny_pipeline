"""
script that takes a directory and makes a fofn list
"""

import glob
import os
import sys

genomes = sys.argv[1]
ext = sys.argv[2]
outfile = sys.argv[3]


def make_fofn(genomes_dir, extension, output_file):
    files = glob.glob(genomes_dir + "/*" + extension)
    print(files)
    with open(output_file, "a") as fout:
        for f in files:
            print(f)
            sample_name = os.path.splitext(os.path.basename(f))[0]
            fout.write("%s\t%s\n" % (sample_name, f))


make_fofn(genomes, ext, outfile)
