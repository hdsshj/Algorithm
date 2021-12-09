class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head   tail
    # [4] -> [2]
    # new_node = Node(3)

    # head   tail
    # [4] -> [2] -> [3]
    # self.tail.next = new_node

    # head          tail
    # [4] -> [2] -> [3]
    # self.tail = new_node

    def enqueue(self, value):
        new_node = Node(3)  # [3]
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        # 어떻게 하면 될까요?
        return

    def peek(self):
        # 어떻게 하면 될까요?
        return

    def is_empty(self):
        # 어떻게 하면 될까요?
        return