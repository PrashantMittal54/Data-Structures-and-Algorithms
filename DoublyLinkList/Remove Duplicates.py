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
            if cur.data == key and cur.next is None and cur == self.head:
                cur.data = None
                cur = None
                self.head = None
                return
            elif cur.data == key and cur == self.head:
                nxt = cur.next
                cur.next = None
                nxt.prev = None
                self.head = nxt
                return
            elif cur.data == key and cur.next is None:
                prev = cur.prev
                cur.prev = None
                cur = None
                prev.next = None
                return
            elif cur.data == key:
                prev = cur.prev
                nxt = cur.next
                prev.next = nxt
                nxt.prev = prev
                cur = None
                return
            cur = cur.next

    def remove_duplicates(self):
        entries = {}
        cur = self.head
        prev = None
        nxt = None
        while cur:
            prev = cur.prev
            nxt = cur.next
            if cur.next is None and cur.data in entries:
                prev.next = None
                cur.prev = None
                cur = None
            elif cur.data in entries:
                prev.next = cur.next
                nxt.prev = cur.prev
                cur = None
            else:
                entries[cur.data] = 1
            cur = nxt


dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)

dllist.print_list()
dllist.remove_duplicates()
print('After')
dllist.print_list()
