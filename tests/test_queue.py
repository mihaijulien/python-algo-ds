import pytest
from lib.datastructures.queue import QueueA

def test_queue():
    queue = QueueA()
    assert queue.is_empty() is True
    queue.enqueue(1)
    assert queue.is_empty() is False
    assert queue.get_size() == 1
    queue.enqueue(2)
    queue.enqueue(3)
    queue.deque()
    assert queue.get_size() == 2
    assert queue.peek() == 2