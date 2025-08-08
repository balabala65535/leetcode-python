"""
双指针
"""
from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


def threeSum(nums):
    """
    自己写的错误答案，[0,0,0] 这种情况无法解
    """
    if len(nums) < 3:
        return []
    elif len(nums) == 3:
        ...

    nums = list(set(nums))
    nums.sort()
    nums_length = len(nums)
    matched = []
    matched_index = []
    for i in range(nums_length):
        for j in range(i, nums_length - 1):
            sum_value = nums[i] + nums[j]
            need_value = 0 - sum_value
            max_value = max(nums[j+1:])
            min_value = min(nums[j+1:])
            if min_value <= need_value <= max_value:
                if need_value in nums:
                    # index_list = nums.index(need_value)
                    index_list = [my_index for my_index, x in enumerate(nums) if x == need_value]
                    k_list = [K for K in index_list if K > j]
                    for k in k_list:
                        # if f"{nums[i]}_{nums[j]}_{nums[k]}" not in matched_index:
                        now_tuple = list([nums[i], nums[j], nums[k]])
                        now_tuple.sort()
                        only_key = "{}_{}_{}".format(*now_tuple)
                        print(only_key)
                        if only_key not in matched_index:
                            matched_index.append(only_key)
                            matched.append([nums[i], nums[j], nums[k]])
    return matched


def threeSum_4(nums):

    n = len(nums)
    res = []
    if (not nums or n < 3):
        return []
    nums.sort()
    res = []
    for i in range(n):
        if (nums[i] > 0):
            return res
        if (i > 0 and nums[i] == nums[i - 1]):
            continue
        L = i + 1
        R = n - 1
        while (L < R):
            if (nums[i] + nums[L] + nums[R] == 0):
                res.append([nums[i], nums[L], nums[R]])
                while (L < R and nums[L] == nums[L + 1]):
                    L = L + 1
                while (L < R and nums[R] == nums[R - 1]):
                    R = R - 1
                L = L + 1
                R = R - 1
            elif (nums[i] + nums[L] + nums[R] > 0):
                R = R - 1
            else:
                L = L + 1
    return res



def threeSum_3(nums):
    """
    1. i != j、i != k 且 j != k
    2. nums[i] + nums[j] + nums[k] == 0
    3.答案中不可以包含重复的三元组
    4.三元组的里的元素，必须是递增
    5.相邻的元素可以相等
    :param nums:
    :return:
    """
    n = len(nums)
    nums.sort()
    ans = list()
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # 去掉相邻相等的
            continue
        print("-------")
        target = - nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                print(f"{i}/{left}/{right}:{nums[i]}/{nums[left]}/{nums[right]}")
                ans.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # 跳过相邻相等的，直到不相等
                    print(f"去掉相邻相等的left:{left}--{nums[left]}")
                    left = left + 1
                while left < right and nums[right] == nums[right - 1]:  # 跳过相邻相等的，直到不相等
                    print(f"去掉相邻相等的right:{right}--{nums[right]}")
                    right -= 1
                right -= 1
                left += 1
    return ans



if __name__ == "__main__":
    # nums = [-1,0,1,2,-1,-4]
    nums = [-1,0,1,2,-1,-4]
    # nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    nums.sort()
    print(nums)
    # nums = [0,1,1]
    # nums = [0,0,0]
    # nums = [1,1,-2]
    # nums = [0,0,0,0]
    # resp = threeSum(nums)
    # resp = threeSum_2(nums)
    # print(resp)

    resp = threeSum_3(nums)
    print(resp)
    resp = threeSum_4(nums)
    print(resp)





