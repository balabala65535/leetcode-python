
from typing import *

class Solution:
    def maxProduct_my(self, nums: List[int]) -> int:
        length = len(nums)
        # INF = 10**1000  # 一个非常大的数
        # max_num = [-float('inf')] * (length)
        max_num = [float('-inf')] * (length)
        min_num = [float('inf')] * (length)
        max_num[0] = nums[0]
        min_num[0] = nums[0]
        for i in range(1, length):
            for j in range(i):
                if nums[i] < 0:
                    max_num[i] = max(nums[i], min_num[j] * nums[i])
                else:
                    max_num[i] = max(nums[i], max_num[j] * nums[i])
                min_num[i] = min(nums[i], max_num[j] * nums[i])

        return max(max_num)

    def maxProduct(self, nums):
        """
        正确
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod  # 交换最大和最小

            # 更新当前最大值和最小值
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            # 更新全局最大值
            result = max(result, max_prod)

        return result

    def maxProduct_2(self, nums):
        """
        解法有问题，[-2,3,-4] 时不能输出 24. [0,2] 不能输出2;
        :param nums:
        :return:
        """

        if not nums:
            return 0

        current_max = current_min = result = nums[0]

        for num in nums[1:]:
            candidates = (current_max * num, current_min * num)
            current_max = max(candidates)
            current_min = min(candidates)

            result = max(result, current_max)

        return result

    def maxProductSubarray(self, nums):
        """
        变种问题：返回子数组本身
        如果需要返回乘积最大的子数组本身，而不仅仅是乘积值：
        :param nums:
        :return:
        """
        if not nums:
            return []

        max_prod = min_prod = result = nums[0]
        start = end = 0
        temp_start = 0

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            if nums[i] > max_prod * nums[i]:
                max_prod = nums[i]
                temp_start = i
            else:
                max_prod = max_prod * nums[i]

            if nums[i] < min_prod * nums[i]:
                min_prod = nums[i]
            else:
                min_prod = min_prod * nums[i]

            if max_prod > result:
                result = max_prod
                start = temp_start
                end = i

        return nums[start:end + 1]