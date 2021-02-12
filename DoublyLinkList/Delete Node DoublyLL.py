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

    def delete(self, key):
        cur = self.head
        while cur:
            if cur == self.head and cur.data == key:
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                if cur.next is not None:
                    pre = cur.prev
                    nxt = cur.next
                    pre.next = nxt
                    nxt.prev = pre
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    pre = cur.prev
                    pre.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
print("Before")
dllist.print_list()
dllist.delete(2)
print("After")
dllist.print_list()
