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


class QuickSort(object):
	def __init__(self, counter=0, last_counter=0):
		self.counter = counter
		self.last_counter = last_counter
		# self.quicksort = QuickSort()

	def quick_sort(self, array):
		quicksort.sort_worker(array, 0, len(array)-1)

	def sort_worker(self, array, first, second):
		
		counter = 0
		if first<second:
			# pivot = partition(array, first, second)
			pivot = quicksort.partition_first(array, first, second)
			counter = counter + (second-first)
			quicksort.sort_worker(array, first, pivot-1)
			quicksort.sort_worker(array, pivot+1, second)

	def partition_first(self, array, first, second):
	
		pivot = array[first]
		array[first]= array[second]
		array[second] = pivot
		i = first + 1
		for j in range(i, second):
			if array[j] < pivot:
				tmp = array[j]
				array[j] = array[i]
				array[i] = tmp
				i += 1
			
				
		tmp = array[first]
		array[first] = array[i-1]
		array[i-1] = tmp

		return i-1

	def partition_last(self, array, left, right):
		pivot = array[right-1]
		array[right-1]= array[left]
		array[left] = pivot
		i = left + 1
		for j in range(i, right):
			if array[j] < pivot:
				tmp = array[j]
				array[j] = array[i]
				array[i] = tmp
				i += 1
				
				
		tmp = array[left]
		array[left] = array[i-1]
		array[i-1] = tmp

		return i-1




if __name__=="__main__":
	quicksort = QuickSort()
	array = [3,9,8,4,6,10,2,5,7,1] # 25-first 29-second.
	quicksort.quick_sort(array)
	# last_quick_sort(array)
	print array
	# print counter
		





