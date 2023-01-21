class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size # create a list with 7 None items in it

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

hash_table = HashTable()

hash_table.print_table()

"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""
print('\n')
hash_table.set_item('hello', 1)
hash_table.set_item('world', 2)
hash_table.set_item('hello', 3)

hash_table.print_table()

"""
    EXPECTED OUTPUT:
    ----------------
0 :  [['hello', 1], ['hello', 3]]
1 :  None
2 :  None
3 :  None
4 :  None
5 :  [['world', 2]]
6 :  None

"""
print('\n')

print(hash_table.get_item('hello')) # 1
print(hash_table.get_item('world')) # 2
print(hash_table.get_item('foobar')) # None
