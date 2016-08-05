# coding: utf-8

'''
in this section we will implement a quicksort algorithm that will take in an 
array of integers and then choose a pivot as well as conduct a sort in increasing
order. The main point of this exercise is that we will be keep track of the number
of comparisons used to sort the array. There are three different rules that shall
be followed in this exercise. You should not count comparisons one-by-one. Rather, 
when there is a recursive call on a subarray of length m, you should simply add m−1
to your running total of comparisons we should always use the first element
of the array as a pivot element for the first part of the assignment.
'''


def quick_sort(ar,m):
	sort_worker(ar, 0, m-1)

def sort_worker(ar, left, right):
	if left < right:
		# print ' '.join(repr(ans)for ans in ar)

		pivot = partition(ar, left, right)
		sort_worker(ar, left, pivot-1)
		sort_worker(ar, pivot+1, right)


def partition(ar, left, right):
	pivot = ar[left]	
	leftmark = left + 1
	rightmark = right

	done = False

	while not done:
		while leftmark <= rightmark and ar[leftmark]<=pivot:
			leftmark +=1
		while ar[rightmark]>=pivot and rightmark>=leftmark:
			rightmark -= 1
		if rightmark < leftmark:
			done = True
		else:
			tmp = ar[leftmark]
			ar[leftmark] = ar[rightmark]
			ar[rightmark] = tmp
			
	tmp = ar[left]
	ar[left] = ar[rightmark]
	ar[rightmark] = tmp
	

	return rightmark
	
def partition_deux(ar, left, right):
	pivot = ar[right]
	i = left
	for j in range(left, right-1):
		if ar[j]<= pivot:			
			tmp = ar[i]
			ar[i] = ar[j]
			ar[j] =tmp
			i +=1
	tmp = ar[right]
	ar[right] = ar[i]
	ar[i] = tmp
	print ar
	return i

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar, m)

print ' '.join(repr(ans)for ans in ar)
		





