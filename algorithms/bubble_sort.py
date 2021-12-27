class BubbleSort:

	def sort(self, array):
		if type(array) is not list:
			raise TypeError("Only lists are allowed")

		for i in range(len(array)):
			for j in range(len(array) - i - 1):
				if(array[j] > array[j+1]):
					array[j], array[j+1] = array[j+1], array[j]
		return array


array = [9,8,7,6,5,4,3,2,1]
bubble = BubbleSort()

print(bubble.sort(array))

