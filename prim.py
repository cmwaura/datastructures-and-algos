'''

in this section we shall take a look at prims algorithm and code up an mst. We will use the
file edges.txt which is an undirected graph with integer edge costs. The format is:

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

where For example, the third line of the file is "2 3 -8874", indicating that there is an edge
connecting vertex #2 and vertex #3 that has cost -8874


PRIM ALGO.
----------
Initialize X = [s] {s in V chosen arbitrarily}.
T != empty [invariant X= Vertices spanned by the tree-so-far]
while X != V:
	let e =(u,v) be the cheapest edge of G with u in C and v in X
	add e to T
	add v to X
i.e increase the # of spanned vertices in the cheapest way.

'''

with open("edges.txt", "r") as fin:
	for lines in fin.readlines():
		tmp = lines.split()
		print tmp
