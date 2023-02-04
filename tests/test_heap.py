import pytest
from datastructures.heap import MinHeap

def test_min_heap():
    heap = MinHeap()
    for i in range(5,0, -1):
        heap.insert(i)


    assert heap.find_mind() == 1
    assert heap.__len__() == 5
    heap.remove()
    assert heap.find_mind() == 2
    assert heap.__len__() == 4