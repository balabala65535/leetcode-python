

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode{{val: {self.val}, next: {repr(self.next)}}}"


def reverseList(head, num=0):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    print(head)
    if head is None or head.next is None:
        # print(head)
        return head

    new_head = reverseList(head.next, num)
    print("org head", head)
    print("new_head：!!!!", new_head)
    # print("####", head)
    head.next.next = head
    # print("--", head)
    head.next = None
    print("*** head.next none new：", head)
    print("========")
    return new_head




def reverseList_1(head, num=0):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    print(head)
    if head is None or head.next is None:
        # print(head)
        return head

    # new_head = reverseList(head.next, num)
    print("org head", head)
    # print("new_head：!!!!", new_head)
    # print("####", head)
    # head.next.next = head
    # # print("--", head)
    # head.next = None
    print("*** head.next none new：", head)
    print("========")
    return reverseList_1(head.next, num)


def my_reverse(cur, pre):
    if cur is None:
        return pre
    level_node = cur.next
    cur.next = pre
    return my_reverse(level_node, cur)


def reverseList_3(head):
    def my_reverse(cur, pre):
        if cur is None:
            return pre
        level_node = cur.next
        cur.next = pre
        return my_reverse(level_node, cur)
    resp = my_reverse(head, None)
    return resp

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val}) -> {repr(self.next)}"


def build_linked_list(lst):
    if not lst:
        return None  # 空列表返回 None
    head = Node(lst[0])               # 当前节点
    head.next = build_linked_list(lst[1:])  # 递归构造剩下的部分
    return head

def end_of_first_half(head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        print("搞了")
        print(fast.next.next)
        print(slow.next)
        fast = fast.next.next
        slow = slow.next
    return slow

if __name__ == "__main__":
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    head = node1

    print('org-->', head)

    head = build_linked_list([1, 2, 3, 4, 5, 4, 3, 2, 1])
    resp = end_of_first_half(head)
    print(resp)
    resp = reverseList_3(resp)
    print(resp)
    # resp = build_linked_list([1, 2,  3])