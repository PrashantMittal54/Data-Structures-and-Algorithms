# Find pairs from a doubly linked list which sum to a specified number.


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

    def pairs_with_sum(self, sum_val):
        pair_dict = {}
        cur = self.head
        output = []
        if not cur:
            return None
        while cur:
            if cur.data not in pair_dict:
                pair_dict[sum_val-cur.data] = cur.data
            else:
                output.append("(" + str(pair_dict[cur.data]) + "," + str(cur.data) + ")")
            cur = cur.next
        return output


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))
