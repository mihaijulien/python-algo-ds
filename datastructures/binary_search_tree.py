class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, key):
        self.__insert(key, self.root)

    def __insert(self, key, node):
        if (node == None):
            return Node(key)

        if (key < node.key):
            node.leftChild = self.__insert(key, node.leftChild)
        elif (key > node.key):
            node.rightChild = self.__insert(key, node.rightChild)
        else:
            return node

    def delete(self, key):
        self.__delete(key, self.root)

    def __delete(self, key, node):
        if(node == None):
            return node

        if(key < node.key):
            node.leftChild = self.__delete(key, node.leftChild)
        elif(key > node.key):
            node.rightChild = self.__delete(key, node.rightChild)
        else:
            if(node.leftChild == None):
                return node.rightChild
            elif(node.rightChild == None):
                return node.leftChild

            node.key = self.__find_min(node.rightChild)
            node.rightChild = self.__delete(key, node.rightChild)


    def find_min(self):
        return self.__find_min(self.root)

    def __find_min(self, node):
        if(node.leftChild == None):
            return node.key

        return self.__find_min(node.leftChild)

    def get_height(self):
        return self.__get_height(self.root)

    def __get_height(self, node):
        if(node == None):
            return 0

        left = self.__get_height(node.leftChild)
        right = self.__get_height(node.rightChild)

        return max(left, right) + 1
