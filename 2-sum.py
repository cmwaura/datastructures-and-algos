'''
The goal of this problem is to implement a variant of the 2-SUM algorithm.
The file contains 1 million integers, both positive and negative 
(there might be some repetitions!).This is your array of integers, with the 
ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000]
(inclusive) such that there are distinct numbers x,y in the input file that satisfy
x+y=t. 

Algorithm.
----------
'''
filename = "algo1-programming_prob-2sum1.txt"
numbers = [int(l) for l in open(filename)]
targets = range(-10000,10001)
H = {}
answers = {}
 
for i in numbers:
  H[i] = True
 
for i in numbers:
  for t in targets:
    if t - i in H:
      if i == t - i:
        continue
      if t not in answers:
        answers[t] = set([tuple(sorted([i, t - i]))])
      else:
        answers[t].add(tuple(sorted([i, t - i])))
 
print len(answers)
