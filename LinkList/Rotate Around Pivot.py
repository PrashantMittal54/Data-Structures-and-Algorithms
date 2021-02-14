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

    def rotate(self, k):
        p = self.head
        q = self.head
        count = 1
        while p and count < k:
            p = p.next
            q = q.next
            count += 1
        if not p:
            return
        while q.next:
            q = q.next
        q.next = self.head
        self.head = p.next
        p.next = None


llist = Linklist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.rotate(4)
llist.print_list()
