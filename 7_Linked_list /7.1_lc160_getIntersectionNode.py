class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __hash__(self):
        return id(self)  # 使用内存地址作为哈希值

    def __eq__(self, other):
        return self is other  # 直接比较是否是同一个对象


def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """

    set_head_a = set(headA)
    for i in headB:
        if i in set_head_a:
            return i
    else:
        return None


def getIntersectionNode_2(headA, headB):
    """
    判断两个链表是否相交，返回相交节点（若相交）
    :param headA: 链表A的头节点
    :param headB: 链表B的头节点
    :return: 相交节点，若不相交返回None
    """
    visited = set()  # 使用集合存储已访问的节点

    # 遍历链表A，将所有节点加入集合
    current = headA
    while current is not None:
        visited.add(current)
        current = current.next

    # 遍历链表B，检查节点是否在集合中
    current = headB
    while current is not None:
        if current in visited:
            return current  # 找到相交节点
        current = current.next

    return None  # 无相交节点

def getIntersectionNode_3(headA, headB):
    """
    替代方案：双指针法（O(1) 空间）
    如果要求空间复杂度为 O(1)，可以用双指针法（无需任何额外存储）：
    :param headA:
    :param headB:
    :return:
    """
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1

def getIntersectionNode_4(headA, headB):
    """
    使用双指针法找到两个链表的相交节点
    :param headA: 链表A的头节点
    :param headB: 链表B的头节点
    :return: 相交节点，若不相交返回None
    这个设计是双指针算法的核心技巧，目的是让两个指针走过相同的总路径长度，从而确保它们会在相交点相遇（或同时到达末尾 None）。
    为None则表示到了链尾了。
    假设：
    链表 A 的非公共部分长度为 a
    链表 B 的非公共部分长度为 b
    公共部分长度为 c
    通过交换路径，两个指针最终走过的总长度相同（a+b+c），因此一定会同时到达相交节点（或同时到达末尾 None）
    """
    if not headA or not headB:
        return None

    pa, pb = headA, headB
    while pa != pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA

    return pa