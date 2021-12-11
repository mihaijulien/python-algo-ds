import pytest
from datastructures.stack import Stack

def test_list():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False
    assert stack.get_size() == 1
    stack.push(2)
    stack.push(3)
    stack.pop()
    assert stack.get_size() == 2
    assert stack.peek() == 2
    stack.clear()
    assert stack.is_empty() == True