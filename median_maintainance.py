# coding: utf-8
'''
The goal of this problem is to implement the "Median Maintenance" algorithm.
The text file contains a list of the integers from 1 to 10000 in unsorted order;
you should treat this as a stream of numbers, arriving one by one. Letting xi 
denote the ith number of the file, the kth median mk is defined as the median 
of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number 
among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 
(i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.

Algorithm covered.
-------------------
'''

import heapq
import sys
filename = "Median.txt"
X = [int(l) for l in open(filename)]
H_low = []
H_high = []
 
sum = 0
for x_i in X:
  if len(H_low) > 0:
    if x_i > -H_low[0]:
      heapq.heappush(H_high, x_i)
    else:
      heapq.heappush(H_low, -x_i)
  else:
    heapq.heappush(H_low, -x_i)
 
  if len(H_low) > len(H_high) + 1:
    heapq.heappush(H_high, -(heapq.heappop(H_low)))
  elif len(H_high) > len(H_low):
    heapq.heappush(H_low, -(heapq.heappop(H_high)))
 
  sum += -H_low[0]
 
print sum % 10000