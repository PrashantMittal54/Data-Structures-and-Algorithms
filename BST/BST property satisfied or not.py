# verify if a binary tree is a BST or not.


class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, current, data):
        if data < current.value:
            if current.left:
                self.insert_helper(current.left, data)
            else:
                current.left = Node(data)
        elif data > current.value:
            if current.right:
                self.insert_helper(current.right, data)
            else:
                current.right = Node(data)
        else:
            print('Value already present.')

    def inorder_print_tree(self):
        if self.root:
            self.inorder_helper(self.root)

    def inorder_helper(self, current):
        if current:
            self.inorder_helper(current.left)
            print(current.value)
            self.inorder_helper(current.right)

    def is_BST_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.value
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(self.root)


bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.is_BST_satisfied())
print(tree.is_BST_satisfied())
