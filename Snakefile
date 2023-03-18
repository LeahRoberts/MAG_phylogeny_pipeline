"""
Pipeline to generate species phylogeny and determine BAPs clusters
"""

configfile: "config.yaml"


rule all:
    input:
        tree = f"{config['out_dir']}/rapidnj.tree",
        cluster_list = f"{config['out_dir']}/mandrake/mandrake.embedding_hdbscan_clusters.csv",
        itol_metadata = f"{config['out_dir']}/itol_metadata.tsv"


rule fofn:
    input:
        MAGs = f"{config['MAG_dir']}/"
    output:
        fofn = f"{config['out_dir']}/fofn.txt"
    script: "scripts/fofn.py"


rule ppsketchlib:
    input:
        fofn = f"{config['out_dir']}/fofn.txt"
    output:
        sketches = f"{config['out_dir']}/ppsketchlib/ppsketchlib.h5",
        distances = f"{config['out_dir']}/ppsketchlib/ppsketchlib_dists_out",
        core_dist = f"{config['out_dir']}/ppsketchlib/ppsketchlib_dists_out.core"
    conda:
        "poppunk"
    threads: 4
    resources:
        mem_mb = 1000
    params:
        prefix = "ppsketchlib"
    shell:
        """
        sketchlib sketch -l {input.fofn} -o {params.prefix} --cpus {threads}
        sketchlib query dist {params.prefix} --cpus {threads} > {output.distances}
        cut -f1-3 {output.distances} > {output.core_dist}
        """


rule distances_to_phylip:
    input:
        core_dist = f"{config['out_dir']}/ppsketchlib/ppsketchlib_dists_out.core"
    output:
        phylip_dist = f"{config['out_dir']}/core_distances.phylip"
    script: "scripts/distances_to_phylip.py"


rule rapidnj:
    input:
        phylip_dist = f"{config['out_dir']}/core_distances.phylip"
    output:
        tree = f"{config['out_dir']}/rapidnj.tree"
    conda:
        "rapidnj"
    threads: 1
    resources:
        mem_mb = 1
    shell:
        "rapidnj {input.phylip_dist} -n -i pd -o t -x {output.tree}"


rule mandrake:
    input:
        sketches = f"{config['out_dir']}/ppsketchlib/ppsketchlib.h5"
    output:
        cluster_list = f"{config['out_dir']}/mandrake/mandrake.embedding_hdbscan_clusters.csv"
    conda:
        "mandrake"
    threads: 4
    resources:
        mem_mb = 2
    shell:
        "mandrake --sketches {input.sketches} --cpus {threads} --kNN 500 --maxIter 10000000 --seed 456"


rule make_itol_output:
    input:
        cluster_list = f"{config['out_dir']}/mandrake/mandrake.embedding_hdbscan_clusters.csv"
    output:
        itol_metadata = f"{config['out_dir']}/itol_metadata.tsv"
    script: "scripts/get_itol_output.py"