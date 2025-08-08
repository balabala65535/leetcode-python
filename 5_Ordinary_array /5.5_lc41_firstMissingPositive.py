
"""
# a = [1, 2, 3, 4]
a = [-1, -2, -6, 0, 3,1,4,5,2]
for i in range(len(a)):
    # print(a[i] - 1, a[i] )
    # res = a[a[i] - 1] == a[i]
    # print(res)
    # while 1 <= a[i] <= len(a) and a[a[i] - 1] != a[i]:
    while a[a[i] - 1] != a[i]:
        a[a[i] - 1],  a[i] = a[i], a[a[i] - 1]
        print(a)
    print("====")
print(a)

"""
from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        无法解决，[1], [2], [1, 1]
        :param nums:
        :return:
        """
        # 获取大于0的整数
        new_nums = [i for i in nums if i >= 1]
        n = len(new_nums)
        if n == 1:
            if nums[0] > 1:
                return 1
            else:
                return 2
        for i in range(1, n):
            if i not in new_nums:
                return i
        return n + 1


def firstMissingPositive(nums):
    """
    91% & 17.03%
    :type nums: List[int]
    :rtype: int
    """
    # 对nums进行排序
    nums = list(set(nums))
    nums.sort()
    odder_than_zorro = [i for i in nums if i >= 1]

    for i, v in enumerate(odder_than_zorro):
        if i + 1 != v:
            min_v = i + 1
            break
    else:
        if odder_than_zorro:
            min_v = nums[-1] + 1
        else:
            min_v = 1

    return min_v

def firstMissingPositive_2(nums):
    """
    80% & 5%, 若去掉nums = list(nums) 为：20%&19%
    :type nums: List[int]
    :rtype: int
    """
    nums = list(nums)
    nums.sort()
    nums.append(None)
    length = len(nums)
    next_expected_v_list = [1] * length
    for i in range(len(nums) - 1):
        if nums[i] <= 0:
            continue
        # 当前值和expected进行比较
        if next_expected_v_list[i] != nums[i]:
            min_v = next_expected_v_list[i]
            break
        # 继续规划下一个数的值
        if nums[i] != nums[i + 1]:
            next_expected_v_list[i + 1] = next_expected_v_list[i] + 1
        else:
            next_expected_v_list[i + 1] = next_expected_v_list[i]
    else:
        min_v = next_expected_v_list[-1]
    return min_v

def firstMissingPositive_1(nums):
    """
    51%&5%
    :param nums:
    :return:
    """
    nums = list(set(nums))
    nums.sort()
    nums.append(None)
    next_expected_v_list = [1]
    for i in range(len(nums) - 1):
        if nums[i] <= 0:
            next_expected_v_list.append(1)
            continue
        # 当前值和expected进行比较
        if next_expected_v_list[-1] != nums[i]:
            min_v = next_expected_v_list[-1]
            break
        # 继续规划下一个数的值
        if nums[i] != nums[i + 1]:
            next_expected_v_list.append(next_expected_v_list[i] + 1)
    else:
        min_v = next_expected_v_list[-1]
    return min_v



def firstMissingPositive_2(nums):
    """
    问题：为什么是x-1的位置，而不是x的位置？
    答：4. 数学一致性
    问题通常要求找到最小的未出现的正整数，而正整数的范围是 1 到 n（数组长度）。将 x 映射到 x-1 可以保证：
    所有正整数 1 ≤ x ≤ n 能严格对应到索引 0 到 n-1。
    遍历时，只需检查 nums[i] == i+1 是否成立即可判断 i+1 是否存在。

    51%&27.12%
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    # 上面步骤将list里的数都变为正数
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])  # 第 x−1 个位置（注意：数组下标从 0 开始）打上「标记」。
    print(nums)
    # 在遍历结束之后，如果所有的位置都被打上了标记，那么答案是 N+1，否则答案是最小的没有打上标记的位置加 1。
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1


def firstMissingPositive_3(nums):
    """
    官方置换法： 如果数组中包含 x∈[1,N]，那么恢复后，数组的第 x−1 个元素为 x。
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(n):  # 相当于排序？
        print('-->',i)
        # 将 nums[i] 放到正确的位置 nums[nums[i]-1]
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            print("###", nums)
            print("***", nums[nums[i] - 1])
        # print(nums)
        # print('--'*5)

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

if __name__ == "__main__":
    # nums = [3,-100,-1,1]
    # nums = [0,2,100,1,1]
    # nums = [1,1,0]
    # nums = [3,4,-1, 1]
    nums = [3,4,-1, 1, 9, 5]
    # nums = [1,2,0]
    # nums = [2]
    # resp = firstMissingPositive(nums)
    resp = firstMissingPositive_2(nums)
    print(resp)