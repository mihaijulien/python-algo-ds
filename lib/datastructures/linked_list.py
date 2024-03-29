class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node;
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node;

    def remove(self, key):
        if(self.head.data == key):
            self.head = self.head.next
        current = self.head
        previous = current
        while(current):
            if(current.data == key):
                current = current.next
                previous.next = current
                return
            previous = current
            current = current.next

    def len_list(self):
        return self.__len_recursive(self.head)

    def __len_recursive(self, node):
        if(node is None):
            return 0
        return 1 + self.__len_recursive(node.next)

    def is_empty(self):
        return self.len_list() == 0

    def contains(self, data):
        if(self.is_empty()):
            return False
        current = self.head
        while(current):
            if(current.data == data):
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        res = ""
        current_node = self.head
        while current_node is not None:
            res += str(current_node.value) + "-> "
            current_node = current_node.next

        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
