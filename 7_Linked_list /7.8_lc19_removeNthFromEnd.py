
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.count = 0

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        递归  100% & 89%
        :param head:
        :param n:
        :return:
        """
        if head is None:
            return None

        head.next = self.removeNthFromEnd(head.next, n)
        self.count += 1

        return head.next if self.count == n else head

    def removeNthFromEnd(self, head, n):
        """
        方法一：计算链表长度

        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        """100%&28%
        为什么可以不使用哑巴节点？
        为什么不需要哑巴节点？
        头节点删除已单独处理：
        当 n == 0 时，直接返回 head.next，避开了头节点删除的特殊情况。
        其他情况直接操作 slow.next：
        slow 最终会指向待删除节点的前驱，因此可以直接修改 slow.next，无需哑巴节点辅助。
        哑巴节点的优势：
        逻辑更统一，无需单独处理头节点删除。
        代码更简洁，适合更复杂的链表操作。
        总结
        方法	优点	缺点
        无哑巴节点	代码较短，直接处理边界情况	需要单独判断 n == 0 的情况
        哑巴节点	逻辑统一，适合复杂操作	多了一个虚拟节点，稍增加空间复杂度
        结论：
        如果问题允许单独处理头节点（如本题），可以不用哑巴节点。
        如果问题涉及多次头节点修改（如合并、反转链表），哑巴节点更稳健。
        你的代码是正确的，但哑巴节点写法更通用，适合面试时快速写出无 bug 的代码。
        """
        slow = head
        fast = head

        while fast:
            fast = fast.next
            n -= 1
            if n < -1:
                slow = slow.next
        if n == 0:
            return head.next

        if slow.next:
            slow.next = slow.next.next

        return head

    def removeNthFromEnd_3(self, head: ListNode, n: int) -> ListNode:
        """
        双指针:快慢指针
        快慢指针法：
        为什么用 dummy 节点好？---哑巴节点
        举个例子：
        如果你要删的是第一个节点（head），那么 slow 是 dummy，slow.next = slow.next.next 仍然有效。
        不需要特别判断 n == len(list) 的时候返回 head.next
        所以它处理边界情况更优雅。

        @派大星学算法 这里并不是要找待删除的节点，而是要寻找待删除节点的前项节点，才能正确删除，对于头结点来说，如果有一个哑节点指向它，就可以不需要额外处理。
        :param head:
        :param n:
        :return:
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy

        # 先让 fast 先走 n + 1 步
        for _ in range(n + 1):
            fast = fast.next

        # 然后 fast 和 slow 同时走
        while fast:
            fast = fast.next
            slow = slow.next

        # 此时 slow 指向的是待删除节点的前一个节点
        slow.next = slow.next.next

        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        :param head:
        :param n:
        :return:
        """
        my_head = ListNode(0, head)
        cur = my_head
        scaned = []
        while cur:
            scaned.append(cur)
            cur = cur.next
        # 更新节点，找到需删除节点的前一个节点
        for _ in range(n):
            scaned.pop()
        dest_node = scaned[-1]
        dest_node.next = dest_node.next.next
        return my_head

