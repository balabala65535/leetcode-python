
def isPalindrome(head):
    """
    复制链表值到数组列表中。51%&19%
    :type head: Optional[ListNode]
    :rtype: bool
    """
    val_list = []
    current = head
    while current:
        val_list.append(current.val)
        current = current.next
    return val_list == val_list[::-1]



def isPalindrome_1(head):
    """
    使用双指针法判断是否为回文。 8%&5%
    :type head: Optional[ListNode]
    :rtype: bool
    """
    # 将链表的值复制到数组中
    val_list = []
    current = head
    while current:
        val_list.append(current.val)
        current = current.next
    length = len(val_list)
    matched = True
    for start, end in zip(range(length), range(length - 1, -1, -1)):
        if val_list[start] != val_list[end]:
            matched = False
    return matched




def isPalindrome_4(head):
    """
    方法三：快慢指针
    :param head:
    :return:
    """
    if head is None:
        return True

    def end_of_first_half(head):
        """
        采用了 快慢指针（Floyd's Tortoise and Hare Algorithm） 的策略来找到链表的中间节点。
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    # 找到前半部分链表的尾节点并反转后半部分链表
    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(first_half_end.next)

    # 判断是否回文
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # 还原链表并返回结果
    first_half_end.next = reverse_list(second_half_start)
    return result


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import *
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        自己实现，71% & 21%
        :param head:
        :return:
        """
        value_list = []
        cur = head
        while cur:
            value_list.append(cur.val)
            cur = cur.next

        # 判断是否为回文
        length = len(value_list)
        mid = length // 2
        for i in range(mid):
            if value_list[i] != value_list[length - i - 1]:
                return False
        return True



if __name__ == "__main__":
    head = [1,2,2,1]
    resp = isPalindrome(head)
    print(resp)