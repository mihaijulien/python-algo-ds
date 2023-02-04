class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# list based
class QueueL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def deque(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

        return value

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        return self.head.value


# array based
class QueueA:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.insert(0, value)

    def deque(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[len(self.queue) - 1]

    def get_size(self):
        return len(self.queue)


queue = QueueA()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.peek())  # 10
print(queue.deque())  # 10
print(queue.deque())  # 20
print(queue.deque())  # 30
# print(queue.deque())  # None
print(queue.is_empty())  # True
