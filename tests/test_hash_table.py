import pytest
from datastructures.hash_table import HashTable

def test_hash_table():
    hash_table = HashTable()
    hash_table.set_item('a', 1)
    hash_table.set_item('a', 2)
    hash_table.set_item('b', 3)

    assert hash_table.get_item('a') == 1
    assert hash_table.get_item('b') == 3
    assert hash_table.get_item('c') is None