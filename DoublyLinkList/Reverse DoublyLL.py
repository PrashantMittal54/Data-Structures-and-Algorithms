class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            prev = cur.prev
            cur.next = cur.prev
            cur.prev = nxt
            cur = nxt
        if not cur:
            self.head = prev.prev


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()
