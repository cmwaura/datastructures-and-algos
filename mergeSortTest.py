import unittest
import itertools
from mergeSort import merge_sort

class MergeSortTest(unittest.TestCase):
	def setUp(self):
		
		with open("test_conversion.txt", "r") as file:
			file = file.read().splitlines()
			self.file = [int(number) for number in file]
			self.sorted_file = sorted(self.file)
			self.mergesort = merge_sort(self.file)
	def test_sort(self):
		for l, obj in itertools.izip(self.sorted_file, self.mergesort):
			self.assertEqual(l, obj)

if __name__ == '__main__':
	unittest.main()