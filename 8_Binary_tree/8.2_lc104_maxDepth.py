def maxDepth(root):
    """
    方法一：深度优先搜索  100%&62%
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root is None:
        return 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1


def maxDepth_1(root):
    """
   广度优先： 69%&53%
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0
    stack = [root]
    length = 0
    while stack:
        son_stack = []
        # 检查是否含有子节点，有就+1
        for node in stack:
            if node.right:
                son_stack.append(node.right)
            if node.left:
                son_stack.append(node.left)
        if son_stack:
            length += 1
        stack = son_stack
    return length + 1


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    """递归实现（DFS）"""
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

def maxDepth(root: TreeNode) -> int:
    """方法二：迭代实现（BFS）"""
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth

def maxDepth(root: TreeNode) -> int:
    """
    方法三：迭代实现（DFS）
    :param root:
    :return:
    """
    if not root:
        return 0
    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
    return max_depth




if __name__ == "__main__":
    from generate_binary_tree import build_tree_from_list, print_tree

    arr = [3,9,20,None,None,15,7]
    root = build_tree_from_list(arr)
    resp = maxDepth_1(root)
    print(resp)
    # print_tree(resp)

