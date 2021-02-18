class Queue:
    def __init__(self):
        self.lists = []

    def enqueue(self, node):
        self.lists.insert(0, node)

    def dequeue(self):
        if self.lists:
            return self.lists.pop()
        else:
            return None

    def peek(self):
        return self.lists[-1].value

    def is_empty(self):
        return len(self.lists) == 0

    def __len__(self):
        return len(self.lists)


class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)

    def reverse_levelOrder_print(self, start):
        if not start:
            return
        Q = Queue()
        Q.enqueue(start)
        traversal = ''
        stack = []
        while len(Q) > 0:
            node = Q.dequeue()
            stack.append(node.value)
            if node.right:
                Q.enqueue(node.right)
            if node.left:
                Q.enqueue(node.left)
        while len(stack) > 0:
            traversal += str(stack.pop()) + '-'
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.reverse_levelOrder_print(tree.root))
