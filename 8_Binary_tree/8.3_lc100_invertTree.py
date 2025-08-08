
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

def invertTree(root):
    """
    100%&85%
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root is None:
        return None
    left_node = invertTree(root.left)
    right_node = invertTree(root.right)
    root.left = right_node
    root.right = left_node
    return root


def invertTree_1(root):
    """
    构造新树
    迭代法：0.1% &9.6%
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root is None:
        return None
    new_tree = TreeNode(root.val)
    stack = [root]
    new_stack = [new_tree]
    while stack:
        son_stack = []
        son_new_stack = []
        for node, new_node in zip(stack, new_stack):
            if node.left:
                son_stack.append(node.left)
                new_node.right = TreeNode(node.left.val)
                son_new_stack.append(new_node.right)
            else:
                new_node.right = None
            if node.right:
                son_stack.append(node.right)
                new_node.left = TreeNode(node.right.val)
                son_new_stack.append(new_node.left)
            else:
                new_node.left = None

        new_stack = son_new_stack
        print("new_stack: ", new_stack)
        stack = son_stack
    return new_tree





def invertTree_2(root):
    """
    BFS 层序遍历（迭代）
    利用队列，从上到下层层遍历，然后在每个节点交换左右子树。
    """
    if not root:
        return None

    queue = deque([root])
    while queue:
        node = queue.popleft()
        # 交换当前节点的左右孩子
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root



def invertTree_4(root):
    """
    DFS（栈模拟前序遍历）
    使用栈手动模拟前序遍历过程：
    :param root:
    :return:
    """
    if not root:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left  # 交换

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


if __name__ == "__main__":
    from generate_binary_tree import build_tree_from_list, print_tree

    arr = [4, 2, 7, 1, 3, 6, 9]
    root = build_tree_from_list(arr)
    resp = invertTree_1(root)
    print_tree(resp)
