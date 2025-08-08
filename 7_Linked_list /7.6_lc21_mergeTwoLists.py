# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode(-1)
    new_chain = dummy
    list1_cur = list1
    list2_cur = list2

    while list1_cur or list2_cur:
        print(list1_cur, list2_cur)
        print("new_chain:", new_chain)
        list1_cur_val = list1_cur.val if list1_cur else 52
        list2_cur_val = list2_cur.val if list2_cur else 52
        if list1_cur_val <= list2_cur_val:
            new_chain.next = list1_cur
            list1_cur = list1_cur.next
        else:
            new_chain.next = list2_cur
            list2_cur = list2_cur.next

        new_chain = new_chain.next
        print("new_chain-->", new_chain)
        print("dummy.next -->", dummy.next)

    # if list1_cur:
    #     new_chain.next = list1_cur
    # if list2_cur:
    #     new_chain.next = list2_cur

    return dummy.next


def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


def mergeTwoLists(l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next