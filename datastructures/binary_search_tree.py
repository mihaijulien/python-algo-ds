class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# iterative
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def __contains__(self, item):
        if self.root.value == item:
            return True
        temp = self.root
        while True:
            if temp.value == item:
                return True
            if temp.value < item:
                if temp.right is None:
                    return False
                temp = temp.right
            else:
                if temp.left is None:
                    return False
                temp = temp.left


# recursive
class RecursiveBinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return self.root
        self.__insert(self.root, value)

    def __insert(self, current_node, value):
        if current_node is None:
            return TreeNode(value)
        if value > current_node.value:
            current_node.right = self.__insert(current_node.right, value)
        else:
            current_node.left = self.__insert(current_node.left, value)
        return current_node

    def delete(self, value):
        self.__delete(self.root, value)

    def __delete(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.__find_min(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete(current_node.right, sub_tree_min)

        return current_node

    def find_mind(self):
        return self.__find_min(self.root)

    def __find_min(self, current_node):
        if current_node.left is None:
            return current_node.value

        return self.__find_min(current_node.left)

    def get_height(self):
        return self.__get_height(self.root)

    def __get_height(self, node):
        if(node == None):
            return 0

        left = self.__get_height(node.left)
        right = self.__get_height(node.right)

        return max(left, right) + 1


tree = RecursiveBinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""

print('Root:', tree.root.value)
print('Root->Left:', tree.root.left.value)
print('Root->Right:', tree.root.right.value)

tree.delete(2)

"""
                 3
                / \
               1   None
"""

print("\nRoot:", tree.root.value)
print("Root.left=", tree.root.left.value)
print("Root.right=", tree.root.right)
