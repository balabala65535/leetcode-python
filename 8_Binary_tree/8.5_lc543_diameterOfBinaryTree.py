def diameterOfBinaryTree_5(root) -> int:
    def max_depth(nodes):
        if nodes is None:
            return 0
        else:
            left_dep = max_depth(nodes.left)
            right_dep = max_depth(nodes.right)
        return max(left_dep, right_dep) + 1

    if root is None:
        return 0
    left_max_dep = max_depth(root.left)
    print(left_max_dep)
    right_max_dep = max_depth(root.right)
    return left_max_dep + right_max_dep

def diameterOfBinaryTree(root) -> int:
    """
    左边最大深度+右边最大深度
    :param root:
    :return:
    """
    max_depth_val = 0
    def max_depth(nodes):
        nonlocal max_depth_val
        if nodes is None:
            return 0
        left_dep = max_depth(nodes.left)
        right_dep = max_depth(nodes.right)
        max_depth_val = max(max_depth_val, left_dep + right_dep)
        return max(left_dep, right_dep) + 1

    if root is None:
        return 0
    left_max_dep = max_depth(root)
    # print(left_max_dep)
    # right_max_dep = max_depth(root.right)
    # print(right_max_dep)
    return max_depth_val



def diameterOfBinaryTree_1(root) -> int:
    """
    23% & 80%
    :param root:
    :return:
    """
    ans = 1
    def depth(node):
        nonlocal ans
        # 访问到空节点了，返回0
        if not node:
            return 0
        # 左儿子为根的子树的深度
        L = depth(node.left)
        # 右儿子为根的子树的深度
        R = depth(node.right)
        # 计算d_node即L+R+1 并更新ans
        ans = max(ans, L + R + 1)
        # 返回该节点为根的子树的深度
        return max(L, R) + 1

    depth(root)
    return ans - 1


def diameterOfBinaryTree_3(root):
    """
    5%&50%
    global：全局作用域（模块级别）；在函数内部修改全局变量；直接查找全局变量；
    变量必须在全局作用域存在；跨函数共享全局状态；
    nonlocal：外层嵌套函数的作用域（非全局）；在嵌套函数内部修改外层函数的变量；
    变量必须在外层函数作用域存在；闭包、嵌套函数的状态维护；
    :param root:
    :return:
    """
    max_diameter = 0  # 用局部变量替代全局变量

    def max_depth(node):
        nonlocal max_diameter  # 使用 nonlocal 修改外部变量
        if node is None:
            return 0
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        max_diameter = max(max_diameter, left_depth + right_depth)  # 更新直径
        return max(left_depth, right_depth) + 1  # 返回当前子树的最大深度

    if root is None:
        return 0
    max_depth(root)  # 计算过程中更新 max_diameter
    return max_diameter


if __name__ == "__main__":
    from generate_binary_tree import build_tree_from_list, print_tree

    arr = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    # arr = [2,97,97,None,47,80,None,-7,None,None,-7]
    root = build_tree_from_list(arr)
    resp = diameterOfBinaryTree(root)
    print(resp)
    # print_tree(root)