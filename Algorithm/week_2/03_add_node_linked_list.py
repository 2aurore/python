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

    def add_node(self, index, value):
        # 추가할 node 객체 생성
        new_node = Node(value)
        # index가 0일 때에 대한 예외처리 수행
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # 추가할 index자리에 해당하는 노드를 가져온다(list는 0부터 시작함으로 -1)
        node = self.get_node(index - 1)
        # 기존 노드의 next인 다음 노드 위치를 저장하는 임시변수
        next_node = node.next
        # 기존 node의 연결고리를 새로운 노드로 연결
        node.next = new_node
        # 새로운 노드의 next에 기존의 next로 가지고 있던 노드 연결
        new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(15)

linked_list.add_node(0, 7)
linked_list.print_all()