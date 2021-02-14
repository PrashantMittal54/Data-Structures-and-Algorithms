class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        if curr is None:
            self.head = new_node
            return
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def reverse_iterative(self):
        if not self.head:
            return
        prev = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev


llist = Linklist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.reverse_iterative()

llist.print_list()
