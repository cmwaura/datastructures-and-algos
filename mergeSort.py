'''
this is a merge sort algorithm that will take in an array of numbers,
preferably from a file then via a fast and conquer algo(mergesort) it
will compute the number of inversions in the array where the i^th row 
indicates the i^th entry of the array
[complete]
'''
inversion_digit =0

def merge_sort(array):
	global inversion_digit
	c = []
	if len(array)> 1:
		mid = len(array) // 2
		left = array[:mid]
		right = array[mid:]

		merge_sort(left)
		merge_sort(right)

			
		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1			
			else:
				array[k] = right[j]
				inversion_digit =inversion_digit+(len(left) - i)
				j += 1
			k += 1
			

		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1	
		return array
if __name__ == '__main__':

	# merge_sort([1,3,5,2,4,6])
	# print inversion_digit
	with open("IntegerArray.txt", "r") as file:
		file = file.read().splitlines()
		file = [int(number) for number in file]	
		merge_sort(file)
		print inversion_digit

