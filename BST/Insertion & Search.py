class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

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

    def search(self, data):
        if self.root:
            return self.search_helper(self.root, data)

    def search_helper(self, current, data):
        if current is None:
            return False
        if current.value == data:
            return True
        elif current.value > data and current.left:
            return self.search_helper(current.left, data)
        elif current.value < data and current.right:
            return self.search_helper(current.right, data)
        else:
            return False


bst = BST(7)
bst.insert(3)
bst.insert(10)
bst.insert(5)
bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(2)
bst.inorder_print_tree()
print(bst.search(11))
