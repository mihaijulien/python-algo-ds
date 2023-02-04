import math


class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __left_child(self, pos):
        return 2 * pos + 1

    def __right_child(self, pos):
        return 2 * pos + 2

    def __parent(self, pos):
        return math.floor(pos / 2)

    def __has_parent(self, pos):
        return self.heap[math.floor(pos / 2)] is not None

    def __has_left_child(self, pos):
        return self.heap[self.__left_child(pos)] is not None

    def __has_right_child(self, pos):
        return self.heap[self.__right_child(pos)] is not None

    def find_min(self):
        if not len(self.heap) == 0:
            return self.heap[0]

    def insert(self, k):
        self.heap.append(k)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.heap) - 1
        while self.__has_parent(index) and self.heap[self.__parent(index)] > self.heap[index]:
            self.heap[self.__parent(index)], self.heap[index] = self.heap[index], self.heap[self.__parent(index)]
            index = self.__parent(index)

    def remove(self):
        if len(self.heap) == 0:
            raise Exception()
        k = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.remove(self.heap[len(self.heap) - 1])
        self.heapify_down(0)
        return k

    def heapify_down(self, pos):
        smallest = pos
        left = self.__left_child(pos)
        right = self.__right_child(pos)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != pos:
            self.heap[pos], self.heap[smallest] = self.heap[smallest], self.heap[pos]
            self.heapify_down(smallest)
