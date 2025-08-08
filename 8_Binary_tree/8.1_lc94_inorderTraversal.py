

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    WHITE, GRAY = 0, 1
    res = []
    print(root)
    stack = [(WHITE, root)]
    print(stack)
    while stack:
        print('--------------')
        color, node = stack.pop() # 移除列表中的最后一个值
        if node is None:
            continue
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)
        print(stack)
    return res

def inorderTraversal_1(root):
    """GPT-递归
    100%&48%"""
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def inorderTraversal_2(root):
    """
    GPT-（非递归，栈模拟）：
    :param root:
    :return:
    """
    stack = []
    res = []
    curr = root

    while curr or stack:
        # 一直往左走，直到没有左孩子
        while curr:
            stack.append(curr)
            curr = curr.left
        # 左到底了，开始回退
        curr = stack.pop()
        res.append(curr.val)
        # 转向右子树
        curr = curr.right

    return res


def inorderTraversal_3(root):
    res = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)
    return res


def inorderTraversal_4(root):
    res = []
    stack = []
    loop_num = 1
    while root or stack:
        print(f"loop_num:{loop_num},{root}")
        loop_num += 1
        while root:
            print(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
        print(res)

    return res


def inorderTraversal_5(root):
    res = []
    while root:
        if root.left:
            # 找前驱节点（左子树中最右的节点）
            predecessor = root.left
            while predecessor.right and predecessor.right != root:
                predecessor = predecessor.right
            if not predecessor.right:
                # 第一次到达 root，把前驱节点的右指针指向 root，继续左走
                predecessor.right = root
                root = root.left
            else:
                # 第二次到达 root，说明左子树已访问完，断开右指针
                res.append(root.val)
                predecessor.right = None
                root = root.right
        else:
            # 没有左子树，直接访问当前节点并向右走
            res.append(root.val)
            root = root.right
    return res

if __name__ == "__main__":
    from generate_binary_tree import build_tree_from_list, print_tree

    arr = [2, 4, 5, None, None, 6, 7]
    root = build_tree_from_list(arr)
    resp = inorderTraversal_4(root)
    print(resp)
    # print_tree(resp)
