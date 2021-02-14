class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        cur1 = self.head
        cur2 = self.head
        prev1 = None
        prev2 = None
        while cur1 and cur1.data != key_1:
            prev1 = cur1
            cur1 = cur1.next
        while cur2 and cur2.data != key_2:
            prev2 = cur2
            cur2 = cur2.next
        if not cur2 or not cur1:
            return
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        cur1.next, cur2.next = cur2.next, cur1.next

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

print("Original List")
llist.print_list()


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()
