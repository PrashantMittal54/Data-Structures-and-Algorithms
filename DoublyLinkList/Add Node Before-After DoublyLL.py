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

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_node_after(self, key, data):
        new_node = Node(data)
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                nxt = cur.next
                cur.next = new_node
                new_node.prev = cur
                new_node.next = nxt
                nxt.prev = new_node
                return
            cur = cur.next

    def add_node_before(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                pre = cur.prev
                new_node = Node(data)
                cur.prev = new_node
                new_node.prev = pre
                pre.next = new_node
                new_node.next = cur
                return
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.print_list()
dllist.add_node_after(3, 6)
dllist.add_node_before(3, 9)
dllist.print_list()

