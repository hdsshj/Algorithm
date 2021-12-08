class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # index    next_node
    # ["자갈"] ["밀가루"] -> ["우편"]
    #          new_node
    #         -> ["흑연"] ->
    # index.nest = new_node
    # new_node.next = next_node
    def add_node(self, index, value):
        new_node = Node(value)
        node = self.get_node(index)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1).data)  # -> 5를 들고 있는 노드를 반환해야 합니다!
