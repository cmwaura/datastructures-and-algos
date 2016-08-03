'''

Your task (should you choose to accept it) is to run Dijkstra's shortest-path 
algorithm on this graph,using 1 (the first vertex) as the source vertex, and
to compute the shortest-path distances between 1 and every other vertex of 
the graph. If there is no path between a vertex v and vertex 1, we'll define 
the shortest-path distance between 1 and v to be 1000000.

Dijkstra's Algorithm:
---------------------
Initialize:
===========
X = [S]
A[S]=0
B[S] = empty path
Main Loop:
==========
while X != V:
	-among all edges (v,w) in E with v in X and w not in X:
			- pick one that minimizes
			(v*, w*) = A[V] + lsub(vw)
			-add w* to X
			-set A[w*] = A[v*] + lsub(vw)
			-set B[w*] = B[v*]U(v*, w*)

'''

with open("dijkstraData.txt") as file:
	vertices = dict()
	for line in file.readlines():
		tmp = line.split()
		try:
			vertices[int(tmp[0])] = {int(x.split(',')[0]):int(x.split(',')[1]) for x in tmp[1:]}
		except Exception, e:
			print "error", e

length = 200
exped = [1]
noexped = list(range(2, length+1))
distance = {x:0 for x in range(1,length+1)}
while len(exped)<length:
	maxlimit = 10**6
	tmpdist = maxlimit
	lenvw = tmpdist
	for v in exped:
		for w in noexped:
			if w in vertices[v].keys():
				lenvw = distance[v] + vertices[v][w]
				if lenvw < tmpdist:
					tmpdist=lenvw
					tmpv, tmpw = v, w

	if tmpdist==maxlimit:break
	exped.append(tmpw)
	noexped.remove(tmpw)
	distance[tmpw] = tmpdist
print distance
print "max distance is" +str(max(distance.values()))
for ind in [7,37,59,82,99,115,133,165,188,197]:
	print str(ind)+ ' is '+ str(distance[ind])