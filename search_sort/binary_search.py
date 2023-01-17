class BinarySearch:

	def __init__(self):
		self.steps = 0

	def contains(self, ordered_list, value):
		if(len(ordered_list)  == 0 or value > ordered_list[len(ordered_list) - 1]):
			return "List doesn't contain the value. Took {0} steps to find.".format(self.steps)

		middle = len(ordered_list) // 2
		first = 0
		last = len(ordered_list) - 1

		while(first <= last):
			self.steps += 1
			middle = (first + last) // 2
			if(value == ordered_list[middle]):
				return "List contains value. Took {0} steps to find.".format(self.steps)
			elif(value > ordered_list[middle]):
				first = middle + 1
			elif(value < ordered_list[middle]):
				last = middle - 1

		return "List doesn't contain the value. Took {0} steps to find.".format(self.steps)

ordered_list = []
for i in range(100):
    ordered_list.append(i)

search = BinarySearch()
print(search.contains(ordered_list, 51))
