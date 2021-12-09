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
        # index에 0이 들어와서 -1이 될 수 있기 때문에 이를 위한 예외처리
        new_node = Node(value)  # [6]
        if index == 0:
            # 새로운 노드를 head노드에 넣기 위해서는 헤드 노드를 new_node에 그냥 넣으면 안됨 -> 이전에 있었던 헤드 노드들이 전부 사라져 버리기 때문이다.
            # 그래서 new_node의 넥스트를 self.head에 미리 정해놓아야한다.
            new_node.next = self.head  # [6] -> [5]
            self.head = new_node  # head -> [6]지정 할 수 있다.
            return

        node = self.get_node(index - 1)  # 0번째 인덱스 [5]
        next_node = node.next  #  [12]
        node.next = new_node  # [5] -> [6]
        new_node.next = next_node  # [6] -> [12]

    def delete_node(self, index):
        return ""


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# [5] -> [12] -> [8]

# print(linked_list.get_node(1).data)  # -> 5를 들고 있는 노드를 반환해야 합니다!
# [5] -> [6] -> [12] -> [8]
linked_list.add_node(1, 6)
linked_list.print_all()