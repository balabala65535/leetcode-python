

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import *
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        new_list = prehead
        pre_num = 0
        level_total = 0
        while l1 or l2:
            if l1 is None:
                l1_va = 0
            else:
                l1_va = l1.val
                l1 = l1.next

            if l2 is None:
                l2_va = 0
            else:
                l2_va = l2.val
                l2 = l2.next

            total = l1_va + l2_va + level_total
            level_total = total // 10
            cur_total = total - level_total * 10
            new_list.next = ListNode(cur_total)
            new_list = new_list.next
        if level_total:
            new_list.next = ListNode(level_total)
        return prehead.next



def addTwoNumbers(l1, l2):
    """
    10%&22% 优化后14%87%
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode(-1)
    add_chain = dummy
    left = 0
    while l1 or l2:
        if l1:
            l1_val = l1.val
            l1 = l1.next
        else:
            l1_val = 0

        if l2:
            l2_val = l2.val
            l2 = l2.next
        else:
            l2_val = 0
        total = l1_val + l2_val + left
        if total >= 10:
            tens, ones = int(str(total)[:-1]), int(str(total)[-1])
            left = tens
        else:
            ones = total
            left = 0
        add_chain.next = ListNode(ones)
        add_chain = add_chain.next

    if left:
        add_chain.next = ListNode(left)
    add_chain = add_chain.next
    return dummy.next




def addTwoNumbers_inplace(l1, l2):
    head = l1  # 最终返回它
    carry = 0
    prev = None

    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        ones = total % 10

        if l1:
            l1.val = ones
            prev = l1
            l1 = l1.next
        else:
            # l1 比 l2 短，接上 l2 剩下的部分
            prev.next = ListNode(ones)
            prev = prev.next

        if l2:
            l2 = l2.next

    # 如果最后还有进位
    if carry:
        prev.next = ListNode(carry)

    return head

def addTwoNumbers(l1, l2):
    """
    有些场景的问题无法解
    l1 = [2,4,9]
    l2 = [9,9,9,9]
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    left = 0
    head = l1
    while l1 or l2 or left:
        l2_val = l2.val if l2 else 0
        l1_val = l1.val if l1 else 0
        total = l1_val + l2_val + left
        left = total // 10
        ones = total % 10
        l1.val = ones

        if l2 and l1.next is None and l2.next:
            l1.next = l2.next

        if l1.next is None and left:
            while left > 0:
                left_1 = left // 10
                ones = left % 10
                l1.next = ListNode(ones)
                l1 = l1.next
                left = left_1
        else:
            l1 = l1.next

        if l2:
            l2 = l2.next
        else:
            l2 = None

    return head