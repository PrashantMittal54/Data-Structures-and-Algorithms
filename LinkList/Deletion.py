# Deletion by Value and Position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def delete_node_at_pos(self, pos):
        cur = self.head
        if pos == 0:
            self.head = cur.next
            cur = None
            return
        count = 0
        prev = None
        while cur and count != pos:
            prev = cur
            cur = cur.next
            count += 1
        if not cur:
            return None
        prev.next = cur.next
        cur = None

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            # cur.data = None
            cur = None
            return
        prev = None
        while cur:
            prev = cur
            cur = cur.next
            if cur and cur.data == key:
                prev.next = cur.next
                # cur.data = None
                cur = None
                return
        else:
            return print('Node does not exist')

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


llist = Linklist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()
llist.delete_node("B")
llist.print_list()
llist.delete_node("E")
llist.delete_node_at_pos(1)
llist.print_list()
