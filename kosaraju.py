'''


in this exercise we will work with a file that contains the edges of 
a graph. Vertices are labelled as positive from 1 - 875714 and every
row indicates an edge with the vertex in the fiirst column being the
tail and the vertex in the second column being the head. 

Task: code an algorithm  for computing SCCs and run the algo on the 
given graph.

Output: the size of the 5 largest SCC's in the graph.

Hint: Kosaraju's algo.
How it works:
1) Let G^(reversed) = G with all arcs reversed
2) run DFS-Loop on G^(reversed)
3) run DFS on G - Discover the SCC's

High-level algorithm:

DFS(G, i):
-----------
1) mark i as explored
2) set leader(i)= nodes
for each(i,j) in G:
	if j not yet explored:
		-DFS(G,j)
t += 1
set f(i):= t

DFS-Loop(G):
------------
global var t = 0
global var s = NULL
Assume nodes in {1,2,...,n}
for i = n down to 1:
	if i not yet explored:
		s(i) = 1
		DFS(G,i)




'''

# adjust the recursion settings provided to python by setting 
# a custom one.

import sys
sys.setrecursionlimit(300000)
text_file = "SCC.txt"
N = 875714


def read_graph():

	graph = {}
	rev_graph = {}
	for i in range(1, N+1):
		graph[i] = [] # create list as values for both the graph and rev_graph
		rev_graph[i] = []
	with open(text_file) as text:
		for line in text:
			v1 = int(line.split()[0]) # basic line splitting and adding the first column as v1
			v2 = int(line.split()[1]) # basic line splitting and adding the second column as v2
			graph[v1].append(v2) # appending the values of v2 into the graph[v1]
			rev_graph[v2].append(v1) # appending the values of v1 into the the rev_graph[v2]
	return graph, rev_graph #return both graphs

visited = {}
leader = {}
finish = {}

def initialize():
	for i in range(1, N+1):
		visited[i] = 0
		finish[i] = 0
		leader[i] = 0j

def dfs(graph, i):
	'''
	DFS(G, i):
	-----------
		1) mark i as explored
		2) set leader(i)= nodes
		for each(i,j) in G:
			if j not yet explored:
				-DFS(G,j)
		t += 1
		set f(i):= t
	'''
	
	global t
	visited[i] = 1
	leader[i] = s

	for _, j in graph.iteritems():
		if visited[j]==0:
			dfs(graph, j)
	t += 1
	finish[i]=t

def dfs_loop(graph):
	'''
	DFS-Loop(G):
	------------
		global var t = 0
		global var s = NULL
		Assume nodes in {1,2,...,n}
		for i = n down to 1:
			if i not yet explored:
				s(i) = 1
				DFS(G,i)
	'''
	global t
	global s
	t = 0 # number of nodes processed so far
	s = 0 # curent source vertex

	i = N
	while(i>0):
		if visited[i] == 0:
			s = i
			dfs(graph, i)
		i -= 1

if __name__ == "__main__":
	'''
	revisit the main idea where we need to:

	1) Let G^(reversed) = G with all arcs reversed
	2) run DFS-Loop on G^(reversed)
	3) run DFS on G - Discover the SCC's

	'''

	graph, rev_graph = read_graph() # get the graphs
	print "dfs on reversed graph"
	dfs_loop(rev_graph) # run the dfs-loop on Grev.

	# construct a new graph
	print "dfs on normal graph"
	new_graph = {}
	for i in range(1, N+1):
		tmp = []
		for x in graph[i]:
			tmp.append(finish[x])
		new_graph[finish[i]] = tmp
	initialize()
	dfs_loop(new_graph)

	# getting the 5 largest SCC's
	print "largest 5 SCC"
	lst = sorted(leader.values()) #sort the values in the leader dict
	statistic = []
	before = 0
	for i in range(0, N-1):
		if lst[i] != lst[i+1]:
			statistic.append(i+1-before)
			before += 1
	statistic.append(N-before)
	L = sorted(statistic)
	L.reverse()
	print L[0:5]



