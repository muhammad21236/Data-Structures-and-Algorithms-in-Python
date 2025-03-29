class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.r_insert(current_node.right, value)
        return current_node

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.r_insert(self.root, value)

    def r_delete(self, current_node, value):
        if current_node is None:
            return None

        if value < current_node.value:
            current_node.left = self.r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.r_delete(current_node.right, sub_tree_min)
        return current_node

    def delete(self, value):
        self.r_delete(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid(self):
        results = self.dfs_in_order()
        for i in range(1, len(results)):
            if results[i] < results[i - 1]:
                return False
        return True


my_tree = BST()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(32)
my_tree.insert(56)
my_tree.insert(88)
# my_tree.insert(20)

print(my_tree.is_valid())
my_tree.delete(47)

print(my_tree.is_valid())

print(my_tree.BFS())
