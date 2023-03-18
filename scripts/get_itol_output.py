import numpy as np


def generate_itol_output(cluster_list, itol_outfile):
    cluster_colours = {}
    used_colours = []
    with open(cluster_list, "r") as fin:
        next(fin)
        for line in fin:
            sample = line.split(",")[0]
            cluster_num = line.split(",")[1].rstrip()
            if cluster_num not in cluster_colours.keys():
                choose_color = False
                while not choose_color:
                    color = list(np.random.choice(range(256), size=3))
                    string = ",".join(map(str, color))
                    rgb = "rbg(" + string + ")"
                    if rgb not in used_colours:
                        used_colours.append(rgb)
                        cluster_colours[cluster_num] = rgb
                        choose_color = True
                    else:
                        pass
            cluster_colour = cluster_colours[cluster_num]
            with open(itol_outfile, "a") as fout:
                fout.write("%s\t%s\t%s\n" % (sample, cluster_colour, cluster_num))

generate_itol_output(snakemake.input.cluster_list, snakemake.output.itol_metadata)

"""
id,hdbscan_cluster__autocolour
GCA_018831525,15
GCF_000273785,27
GCF_006742345,83
GCF_018289175,12
GCF_018289375,41
GCF_018291785,2
GCF_018292165,27
GCF_900896415,45
MGYG000001346,5
MGYG000004948,69
MGYG000004993,41
MGYG000005007,41
MGYG000005325,27
MGYG000005413,23
MGYG000005430,41
MGYG000005673,41
"""