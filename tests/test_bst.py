import pytest
from datastructures.binary_search_tree import RecursiveBinarySearchTree

def test_tree():
	bst = RecursiveBinarySearchTree()
	bst.insert(10)
	assert bst.get_height() == 1

	bst.insert(5)

	assert bst.get_height() == 2
	assert bst.find_min() == 5

	bst.delete(5)
	assert bst.get_height() == 1
