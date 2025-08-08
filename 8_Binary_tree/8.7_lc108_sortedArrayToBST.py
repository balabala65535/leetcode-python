"""
1. 这不是平衡树，而题目要求的是高度平衡的BST（左右子树高度差 ≤ 1）。
2. 二叉搜索树是一种特殊的二叉树，满足以下性质：
左子树的所有节点值 < 根节点值
右子树的所有节点值 > 根节点值
左右子树也必须是二叉搜索树（递归定义）

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    """
    生成的数列 不平衡
    :param nums:
    :return:
    """
    def generate_tree(num_list):
        length = len(num_list)
        prev = TreeNode(num_list[0])
        for i in range(1, length):
            prev.right = TreeNode(num_list[i])
        return prev

    if not nums:
        return None
    length = len(nums)
    if length in [1, 2]:
        return generate_tree(nums)
    else:
        top_node = TreeNode(nums[length // 2])
        left_nodes = generate_tree(nums[:length // 2])
        right_nodes = generate_tree(nums[(length // 2) + 1:])
        top_node.left = left_nodes
        top_node.right = right_nodes
        return top_node



def sortedArrayToBST_1(nums):
    """
    生成的数列 不平衡
    :param nums:
    :return:
    """
    from collections import deque

    def generate_tree(num_list):
        length = len(num_list)
        my_root = TreeNode(num_list[0])
        node_deque = deque([my_root])
        i = 1
        while node_deque and i < length:
            cur_node = node_deque.popleft()
            cur_node.left = TreeNode(num_list[i])
            node_deque.append(cur_node.left)
            i += 1
            if i < length:
                cur_node.right = TreeNode(num_list[i])
                node_deque.append(cur_node.right)
        return my_root
    if not nums:
        return None
    length = len(nums)
    if length in [1, 2]:
        return generate_tree(nums)
    top_node = TreeNode(nums[length // 2])
    left_nodes = generate_tree(nums[:length // 2][::-1])
    right_nodes = generate_tree(nums[length // 2 + 1:][::-1])
    top_node.left = left_nodes
    top_node.right = right_nodes
    return top_node



def sortedArrayToBST_6(nums):
    """
    11%42% --> 39%&53%
    . 切片操作 nums[:mid] 的时间复杂度
    时间复杂度：O(k)，其中 k 是切片长度（这里是 mid）

    原理：切片操作需要创建新列表并复制原列表中指定范围的元素

    :param nums:
    :return:
    """
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


def sortedArrayToBST_5(nums   ):
    """
    85% & 65%
    :param nums:
    :return:
    """

    def helper(left, right):
        if left > right:
            return None

        # 总是选择中间位置左边的数字作为根节点
        mid = (left + right + 1) // 2

        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(nums) - 1)

from typing import *

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)



if __name__ == "__main__":
    from generate_binary_tree import build_tree_from_list, print_tree, print_tree_horizontal

    # nums = [-1, 0, 1, 2]
    nums = [-2, -1, 0,1,2,3,4,5, 6, 7]
    # nums = [1, 3]
    resp = sortedArrayToBST_5(nums)
    print_tree_horizontal(resp)
