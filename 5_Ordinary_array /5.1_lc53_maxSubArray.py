
def maxSubArray(nums):
    """
    错误解法
    :type nums: List[int]
    :rtype: int
    """
    sum_list = []
    top_num = nums[0]

    for my_index, i in enumerate(nums):
        if my_index == 0:
            sum_list.append(i)
            continue
        sum_list = list(map(lambda x: x + i, sum_list))
        sum_list.append(i)
        top_num = max(max(sum_list), top_num)
    return top_num


def maxSubArray_1(nums):
    """
    动态规划
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    sum_max = nums[0]
    for i in range(1, length):
        if nums[i] + nums[i-1] > nums[i]:
            nums[i] += nums[i-1]

        if nums[i] > sum_max:
            sum_max = nums[i]
    print(nums)
    return sum_max


def maxSubArray_2(nums):
    """
    动态规划--慕强，不要猪队友，你有价值才让你加入我的队伍，不然就舍弃，三角金字塔，对我有利的我才要，不然就不要。
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    sum_max = nums[0]
    for i in range(1, length):
        if nums[i-1] > 0:  # 对我有利的我才要，不然就不要。
            nums[i] += nums[i-1]
        if nums[i] > sum_max:  # 每一次都取判断一下和sum_max比较
            sum_max = nums[i]
    return sum_max


from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = max_sum = nums[0]
        for i in nums[1:]:
            pre = max(pre + i,  i)
            max_sum = max(max_sum, pre)
        return max_sum


def maxSubArray_3(nums):
    """
    分治
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    sum_max = nums[0]
    for i in range(1, length):
        if nums[i-1] > 0:  # 对我有利的我才要，不然就不要。
            nums[i] += nums[i-1]
        if nums[i] > sum_max:  # 每一次都取判断一下和sum_max比较
            sum_max = nums[i]
    return sum_max

def maxSubArray_4(nums) -> int:
    """
    前缀和--由于子数组的元素和等于两个前缀和的差，所以求出 nums 的前缀和，
    :param nums:
    :return:
    """
    ans = nums[0]
    min_pre_sum = pre_sum = 0
    for x in nums[1:]:
        pre_sum += x  # 当前的前缀和
        ans = max(ans, pre_sum - min_pre_sum)  # 减去前缀和的最小值
        min_pre_sum = min(min_pre_sum, pre_sum)  # 维护前缀和的最小值
    return ans


def maxSubArray_5(nums) -> int:
    """
    同-4的思路，但是不是该题的解
    :param nums:
    :return:
    """
    length = len(nums)
    sum_max = 0
    ans = nums[0]
    for i in range(1, length):
        sum_max += nums[i]
        ans = max(ans, sum_max)
        if sum_max <= 0:
            sum_max = 0
    return ans



if __name__ == "__main__":
    # nums = [-2,-1,3,4,1,-2,1,-5,20]
    nums = [2, 0, -1, 3]

    # resp = maxSubArray(nums)
    # resp = maxSubArray_1(nums)
    resp = maxSubArray_5(nums)
    print(resp)