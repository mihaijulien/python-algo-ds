class Stack:

    def __init__(self):
        self.stackList = []
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def push(self, key):
        self.stackList.append(key)
        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.stackList.pop()
        self.size -= 1

    def peek(self):
        return None if self.is_empty() else self.stackList[self.get_size() - 1];

    def get_size(self):
        return self.size;

    def clear(self):
        self.stackList = []
        self.size = 0