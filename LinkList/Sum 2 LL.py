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

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        s = Linklist()
        while p or q:
            if p:
                i = p.data
            else:
                i = 0
            if q:
                j = q.data
            else:
                j = 0
            sum = i + j + carry
            if sum >= 10:
                carry = 1
                s.append(sum % 10)
            else:
                s.append(sum)
                carry = 0
            p = p.next
            q = q.next
        return s


llist1 = Linklist()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = Linklist()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
llist3 = llist1.sum_two_lists(llist2)
llist3.print_list()