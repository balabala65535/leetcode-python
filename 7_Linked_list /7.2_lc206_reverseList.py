
def reverseList(head):
    """
    迭代的方式
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def reverseList_1(head):
    """
    100%&58%
    :param head:
    :return:
    """
    have_scanned = None
    current_scan_node = head
    while current_scan_node:
        need_scan_node = current_scan_node.next
        # 把当前节点当作have_scanned 的head, 并加上have_scanned
        current_scan_node.next = have_scanned
        # 更新have_scanned
        have_scanned = current_scan_node
        # 更新后面需要scan的node
        current_scan_node = need_scan_node
    return have_scanned

def reverseList_2(head):
    """
    递归 12%&%
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head

    new_head = reverseList_2(head.next)
    head.next.next = head  # 形成了闭环（循环链表）
    head.next = None  # 将环打开
    return new_head


def my_reverse(cur, pre):
    if cur is None:
        return pre
    level_node = cur.next
    cur.next = pre
    return my_reverse(level_node, cur)

def reverseList_3(head):
    """
    12%&5%
    在性能上通常会“更慢”或“更劣”，这是因为它有额外的空间和函数调用开销。
    这是一种 “隐式的”性能消耗
    而循环 + 双指针的方式就没有这些栈的操作，所以实际跑起来要快很多。
    :param head:
    :return:
    """
    resp = my_reverse(head, None)
    return resp


def reverseList_4(head):
    cur, pre = head, None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre
