class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# list based
class StackL:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value


# array based
class StackA:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.insert(0, value)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop(0)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[0]

    def get_size(self):
        return len(self.stack)

    def clear(self):
        self.stack = [] 


stack = StackA()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())  # 30
print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.pop())  # 10
#print(stack.pop())   # None
print(stack.is_empty())  # True
