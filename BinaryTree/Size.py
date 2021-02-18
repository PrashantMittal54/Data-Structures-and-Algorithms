class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)

    def size(self, data):
        if data is None:
            return 0
        left_size = self.size(data.left)
        right_size = self.size(data.right)
        return 1 + left_size + right_size


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.size(tree.root))
