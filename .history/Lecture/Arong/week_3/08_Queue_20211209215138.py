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
        # head와 tail에 아무것도 없는 None일 경우 예외처리
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # head          tail
    # [4] -> [2] -> [3]

    # delete_head = self.head

    # self.head = self.head.next
    #        head   tail
    # [4] -> [2] -> [3]

    # return delete_head
    # head   tail
    # [2] -> [3]   반환! [4]

    def dequeue(self):
        delete_head = self.head
        self.head = self.head.next

        return delete_head

    def peek(self):
        # 어떻게 하면 될까요?
        return

    def is_empty(self):
        # 어떻게 하면 될까요?
        return