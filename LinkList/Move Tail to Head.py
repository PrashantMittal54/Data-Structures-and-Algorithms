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

    def move_tail_to_head(self):
        if not self.head:
            return
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        curr.next = self.head
        self.head = curr
        prev.next = None


llist = Linklist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# llist.print_list()
llist.move_tail_to_head()
llist.print_list()
