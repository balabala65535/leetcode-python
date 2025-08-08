
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None  # 初始为空链表

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # 删除成功
            prev = current
            current = current.next
        return False  # 未找到

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')



ll = LinkedList()
ll.append(10)
ll.append(20)
ll.insert_at_head(5)
ll.print_list()  # 输出：5 -> 10 -> 20 -> None

ll.delete(10)
ll.print_list()  # 输出：5 -> 20 -> None
