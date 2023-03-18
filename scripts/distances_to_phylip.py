import sys

def distances_to_phylip(core_distance_file, outfile):
	dic_matrix = {}
	list_order = []
	with open(core_distance_file, "r") as core_in:
		next(core_in)
		for line in core_in:
			query = line.split()[0]
			ref = line.split()[1]
			dist = line.split()[2]
			if query not in list_order:
				list_order.append(query)
			if query not in dic_matrix.keys():
				dic_matrix[query] = {}
			if ref not in dic_matrix.keys():
				dic_matrix[ref] = {}
			dic_matrix[query][query] = 0
			dic_matrix[query][ref] = dist
			dic_matrix[ref][query] = dist
			dic_matrix[ref][ref] = 0
	with open(outfile, "a") as fout:
		ref_num = len(list_order)
		fout.write("%s\n" % ref_num)
		for sam in list_order:
			distances_list = []
			for sam2 in list_order:
				out_dist = dic_matrix[sam][sam2]
				distances_list.append(str(out_dist))
			distances_string = " ".join(distances_list)
			fout.write("%s %s\n" % (sam, distances_string))

distances_to_phylip(snakemake.input.core_dist, snakemake.output.phylip_dist)