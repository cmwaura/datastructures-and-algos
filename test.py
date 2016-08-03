def quick_sort(array):
	sort_worker(array, 0, len(array)-1)

def sort_worker(array, first, second):
	'''
	this is where the recursion will take placethe sort_worker until the whole 
	process is done. The quick sort algorithm at this point is:
	if n = 1(where n is the length) return
	choose a pivotpoint(Array,n)
	partition around P [ <P,P,>P]
	recursively sort part1 
	recursively sort part2
	'''
	global counter
	if first<second:
		# pivot = partition(array, first, second)
		pivot = partition(array, first, second)
		counter = counter + (second-first)
		sort_worker(array, first, pivot-1)
		sort_worker(array, pivot+1, second)

def partition(array, first, second):
	
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

	
	# pivot = array[first]
	# left = first + 1
	# right = second
	# checkmate = False

	# while not checkmate:
	# 	# here we are going to direct the left to move towards
	# 	# the right as we move the right towards the left:
	# 	# hence left += 1 and right -= 1

	# 	while left<=right and array[left]<=pivot:
	# 		left += 1
	# 	while right >= left and array[right]>= pivot:
	# 		right -= 1
		
	# 	# now that we have done that we need to apply a swap when
	# 	# the left< pivot 
	# 	if right < left:
	# 		checkmate = True

	# 	else:
	# 		# the swap begins
	# 		temp = array[left]
	# 		array[left]= array[right]
	# 		array[right] = temp
			
	
	# temp = array[first]
	# array[first] = array[right]
	# array[right] = temp
	# return right

def last_quick_sort(array):
	last_sort_worker(array, 0, len(array))

def last_sort_worker(array, left, right):
	'''
	this is where the recursion will take placethe sort_worker until the whole 
	process is done. The quick sort algorithm at this point is:
	if n = 1(where n is the length) return
	choose a pivotpoint(Array,n)
	partition around P [ <P,P,>P]
	recursively sort part1 
	recursively sort part2
	'''
	global last_counter
	if left<right:
		# pivot = partition(array, first, second)
		pivot = partition_last(array, left, right)
		last_counter += (right-left-1)
		last_sort_worker(array, left, pivot-1)
		last_sort_worker(array, pivot+1, right)


def partition_last(array, left, right):
	'''
	question1: we choose the first element of the array as the initial pivot
	the main algo for the partition is:
	input = Array[L,....,R]
	pivot :=A[L]
	i = l+1
	for j=L+1 to R:
		if A[j] < P:
			swap A[j] and A[i]
			i +=a
		swap A[i] and A[i-1]
	'''
	
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
	# with open("IntegerArray.txt", "r") as file:
	# 	file = file.read().splitlines()
		# test4 = []
		# for i in range(1, 101):
		# 	test4.append(i)
		# print test4
		# array = [int(number) for number in file]
		array = [3,9,8,4,6,10,2,5,7,1] # 25-first 29-second.
		quick_sort(array)
		last_quick_sort(array)
		print array
		print counter
		
