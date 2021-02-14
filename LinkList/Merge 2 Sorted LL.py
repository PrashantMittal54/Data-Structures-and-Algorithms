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


def merge_linklist(llist1, llist2):
    if not llist1:
        return llist2
    if not llist2:
        return llist1
    p = llist1.head
    q = llist2.head
    s = Linklist()
    while p and q:
        if p.data < q.data:
            s.append(p.data)
            p = p.next
        else:
            s.append(q.data)
            q = q.next
    if not p and not q:
        return s
    elif not p:
        while q:
            s.append(q.data)
            q = q.next
    elif not q:
        while p:
            s.append(p.data)
            p = p.next
    return s


llist_1 = Linklist()
llist_2 = Linklist()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_3 = merge_linklist(llist_1, llist_2)
llist_3.print_list()
