
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric_1(root):
    """
    递归
    :param root:
    :return:
    """
    if root is None:
        return True

    def checking_symmetric(nodes_1, nodes_2):
        if nodes_1 is None and nodes_2 is None:
            return True
        if nodes_1 is None or nodes_2 is None:
            return False

        return nodes_1.val == nodes_2.val and checking_symmetric(nodes_1.left, nodes_2.right) and checking_symmetric(nodes_1.right, nodes_2.left)
    return checking_symmetric(root.left, root.right)



def isSymmetric_2(root):
    """
    迭代-- 分层检查版: 100% & 5%
    一层一层的找，left_val = right_val到倒序，长度必为偶数
    :param root:
    :return:
    """
    def checking_symmetric(node_list):
        length = len(node_list)
        if length % 2 != 0:
            return False
        left_list = node_list[0: length // 2]
        right_list = node_list[length // 2:][::-1]
        for left, right in zip(left_list, right_list):
            if left is None and right is None:
                continue
            if left is None or right is not None:
                return False
            if left.val != right.val:
                return False
        else:
            return True

    stack = [root]
    while stack:
        son_stack = []
        for node in stack:
            if node is None:
                continue
            son_stack.append(node.left)
            son_stack.append(node.right)
        # 检查son_stack 是否对称
        # print([i.val if i else None for i in son_stack])
        is_symmetric = checking_symmetric(son_stack)
        if not is_symmetric:
            return False
        stack = son_stack
    else:
        return True


def isSymmetric_3(root) -> bool:
    """
    BFS 队列版 9% & 5%


    list.pop(0) 的时间复杂度是 O(n)

    list.pop()（移除最后一个元素）的时间复杂度是 O(1)



    :param root:
    :return:
    """
    if not root:
        return True

    queue = []
    queue.append(root)
    queue.append(root)

    while queue:
        u = queue.pop(0)
        v = queue.pop(0)

        if u is None and v is None:
            continue
        if u is None or v is None:
            return False
        if u.val != v.val:
            return False

        queue.append(u.left)
        queue.append(v.right)

        queue.append(u.right)
        queue.append(v.left)

    return True


def isSymmetric_4(root) -> bool:
    """
    100%&92%
    :param root:
    :return:
    """
    from collections import deque
    if not root:
        return True

    q = deque()
    q.append(root)
    q.append(root)

    while q:
        u = q.popleft()
        v = q.popleft()

        if u is None and v is None:
            continue
        if u is None or v is None:
            return False
        if u.val != v.val:
            return False

        q.append(u.left)
        q.append(v.right)
        q.append(u.right)
        q.append(v.left)

    return True

if __name__ == "__main__":
    from generate_binary_tree import build_tree_from_list, print_tree

    # arr = [1,2,2,3,4,4,3]
    # arr = [1,2,2,3,4,4,3, 5, 6, 7, 8, 8, 7, 5, 8]
    # arr = [1,2,2,None,3,None,3]
    arr = [2,97,97,None,47,80,None,-7,None,None,-7]
    root = build_tree_from_list(arr)
    resp = isSymmetric_2(root)
    print(resp)