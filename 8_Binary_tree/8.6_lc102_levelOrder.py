


def levelOrder(root):
    """
    23% & 97%

    每次 for node in stack 时，Python 的 list 是动态数组，pop(0) 需要移动后面的所有元素，导致性能下降。
    隐式依赖 list 的迭代，但没有显式控制当前层的节点数量。
    可能导致不必要的检查。
    :param root:
    :return:
    """
    if root is None:
        return []
    tree_list = []
    stack = [root]
    while stack:
        son_stack = []
        stack_val = []
        for node in stack:
            stack_val.append(node.val)
            if node.left:
                son_stack.append(node.left)
            if node.right:
                son_stack.append(node.right)
        stack = son_stack
        tree_list.append(stack_val)
    return tree_list


def levelOrder_fast(root):
    """
    如果仍想用 list，可以改用索引模拟队列，避免 pop(0)：
    23% & 5%
    :param root:
    :return:
    """
    if not root:
        return []
    result = []
    queue = [root]
    i = 0
    while i < len(queue):
        level_size = len(queue) - i
        current_level = []
        for _ in range(level_size):
            node = queue[i]
            i += 1
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result

def levelOrder_3(root):
    """
    100%&87%
    :param root:
    :return:
    """
    from collections import deque
    result = []
    if not root:
        return result

    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()  # O(1) 操作
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result


def levelOrder_1(root):
    """
    100%&41%
    显式控制当前层节点数量，避免多余遍历。
    更精准地处理每一层，减少无效操作。
    :param root:
    :return:
    """
    result = []
    if not root:
        return result

    queue = [root]
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.pop(0)  # 从队列头部取出节点  pop 第一个节点, O(n)操作
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result

