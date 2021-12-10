import pytest
from datastructures.linked_list import LinkedList

def test_list():
	llist = LinkedList()
	assert llist.is_empty() is True

	llist.add(1)
	assert llist.is_empty() is False
	assert llist.len_list() == 1
	assert llist.contains(1) is True
	llist.add(2)
	llist.add(3)
	llist.remove(2)
	assert llist.len_list() == 2
