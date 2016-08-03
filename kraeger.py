import copy
from random import randint


'''
Your task is to code up and run the randomized contraction algorithm for the min cut
problem and use it on the above graph to compute the min cut. 
(HINT: Note that you'll have to figure out an implementation of edge contractions. 
Initially, you might want to do this naively, creating a new graph from the old every 
time there's an edge contraction. But you should also think about more efficient implementations.) 
(WARNING: As per the video lectures, please make sure to run the algorithm many times with different 
random seeds, and remember the smallest cut that you ever find.) Write your numeric 
answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.

'''


with open("kargerMinCut.txt", "r") as file:
	graph_dict = {}
	for line in file:
		l = [int(s) for s in line.split()]
		
		graph_dict[l[0]] = l[1:]

def choose_rand_edge(graph_dict):
	v1 = graph_dict.keys()[randint(0, len(graph_dict)-1)]
	v2 = graph_dict[v1][randint(0, len(graph_dict[v1])-1)]
	return v1, v2

def karger_step(graph_dict):
	#generate v1 and v2
	v1, v2 = choose_rand_edge(graph_dict)
	# contract v1 and v2 together
	graph_dict[v1].extend(graph_dict[v2])
	# replace all instances of v2 as v1
	for x in graph_dict[v2]:
		l = graph_dict[x]
		for i in range(0, len(l)):
			if l[i] == v2:
				l[i] = v1
	# remove the self loops
	while v1 in graph_dict[v1]:
	 	graph_dict[v1].remove(v1)
	# remove v2 list
	del graph_dict[v2]

def karger(graph_dict):
	while len(graph_dict)>2:
		karger_step(graph_dict)
	return len(graph_dict[graph_dict.keys()[0]])

m = karger(copy.deepcopy(graph_dict))
for i in range(0, 1000):
	instance = karger(copy.deepcopy(graph_dict))
	if instance < m:
		m = instance
	print "final:", m 


