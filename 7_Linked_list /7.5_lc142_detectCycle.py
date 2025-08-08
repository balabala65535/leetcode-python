
def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    see = set()
    while head:
        if head in see:
            return head
        see.add(head)
        head = head.next
    return None

def detectCycle(head):
    """
    检测链表是否有环，并返回环的起始节点
    :param head: 链表头节点
    :return: 环的起始节点（若无环返回None）
    """
    slow, fast = head, head
    while fast is not None:
        slow = slow.next
        if fast.next is None:
            return None
        fast = fast.next.next
        if fast == slow:
            p = head
            while p != slow:
                p = p.next
                slow = slow.next
            return p
    return None



if __name__ == "__main__":
    from linked_list_leetcode import build_linked_list

    head = build_linked_list([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
    resp = detectCycle(head)
    print(resp)