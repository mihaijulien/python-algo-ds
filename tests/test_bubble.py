import pytest
from search_sort.bubble_sort import BubbleSort

array_under_test = [9,8,7,6,5,4,3,2,1]
expected = [1,2,3,4,5,6,7,8,9]

bubble = BubbleSort()

def test_bubble_sort():
    assert bubble.sort(array_under_test) == expected

def test_type_exception():
	with pytest.raises(TypeError) as excinfo:
		bubble.sort("wrong_type")
	assert str(excinfo.value) == "Only lists are allowed"
