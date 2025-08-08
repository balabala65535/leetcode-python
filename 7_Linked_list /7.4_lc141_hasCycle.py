def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    seen = set()
    while head:
        # print(head)
        if head in seen:
            return True
        seen.add(head)
        head = head.next
        print(seen)
    return False


def hasCycle_1(head):
    slow = fast = head  # 乌龟和兔子同时从起点出发
    while fast and fast.next:
        slow = slow.next  # 乌龟走一步
        fast = fast.next.next  # 兔子走两步
        if fast is slow:  # 兔子追上乌龟（套圈），说明有环
            return True
    return False  # 访问到了链表末尾，无环


def hasCycle_2(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


def hasCycle_3(head):
    """
    过河拆桥法
    :param head:
    :return:
    """
    if head is None:
        return False
    while head.next is not None:
        head.val = None
        head = head.next
        if head.val is None:
            return True
    return False


if __name__ == "__main__":
    from linked_list_leetcode import build_linked_list

    head = build_linked_list([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
    resp = hasCycle(head)
    print(resp)
