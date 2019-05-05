import unittest
import QuickSort
import MergeSort
from random import randint


class SortTest(unittest.TestCase):
    def test_quicksort(self):
        for i in range(10):
            l = [randint(-1000000, 100000000) for x in range(100000)]
            self.assertEqual(QuickSort.quickSort(l), sorted(l))

    def test_MergeSort(self):
        for i in range (10):
            l = [randint(-1000000, 100000000) for x in range(100000)]
            self.assertEqual(MergeSort.mergeSort(l), sorted(l))


if __name__ == '__main__':
    unittest.main()