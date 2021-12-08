class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node
print(node.next.data)

print(node.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)


linked_list = LinkedList(3)
print(linked_list.head.data)
