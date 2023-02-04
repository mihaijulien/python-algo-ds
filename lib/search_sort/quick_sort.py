class Quicksort:

    def __init__(self, array):
        self.steps = 0
        if isinstance(array, list):
            self.array = array
        else:
            raise Exception("Only lists are allowed")

    def sort(self):
        self.__quicksort(self.array, 0, len(self.array) - 1)

    def __quicksort(self, array, left, right):
        if left < right:
            pivot = self.partition(array, left, right)
            self.__quicksort(array, left, pivot - 1)
            self.__quicksort(array, pivot + 1, right)

        return array

    def partition(self, array, start_index, pivot_index):
        i = start_index - 1
        pivot = array[pivot_index]

        for j in range(start_index, pivot_index+1):
            if array[j] < pivot:
                i += 1
                array[j], array[i] = array[i], array[j]

        array[i + 1], array[pivot_index] = array[pivot_index], array[i + 1]

        return i + 1


my_list = [4, 6, 1, 7, 3, 2, 5]

alg = Quicksort(my_list)
alg.sort()

print(my_list)

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
 """
