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

    def is_palindrome(self):
        if self.head:
            p = self.head
            q = self.head
        else:
            return False
        count = 0
        qlist = []
        while q:
            qlist.append(q.data)
            q = q.next
            count += 1
        num = 1
        while num <= count//2 + 1:
            if qlist[-num] != p.data:
                return False
            p = p.next
            num += 1
        else:
            return True


llist_2 = Linklist()
llist_2.append("R")
llist_2.append("A")
llist_2.append("D")
llist_2.append("A")
llist_2.append("R")

print(llist_2.is_palindrome())
