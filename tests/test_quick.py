import pytest
from search_sort.quick_sort import Quicksort

array_under_test = [9,8,7,6,5,4,3,2,1]
expected = [1,2,3,4,5,6,7,8,9]

quick = Quicksort(array_under_test)

def test_quick_sort():
	quick.sort()
	assert array_under_test == expected
