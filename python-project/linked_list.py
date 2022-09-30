class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            return 
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print (elements)

def main():
    llist = LinkedList()
    llist.append('A')
    llist.append('B')
    llist.append('C')
    llist.append('D')

    llist.insert_after_node(llist.head.next, "E")

    # llist.prepend('E')
    llist.print_list()
main()