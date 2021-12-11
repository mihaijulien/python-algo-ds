class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.insert(0, data)

    def deque(self):
        if not self.is_empty():
            self.queue.pop()
        
    def peek(self):
        return None if self.is_empty() else self.queue[self.get_size() - 1]

    def get_size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0