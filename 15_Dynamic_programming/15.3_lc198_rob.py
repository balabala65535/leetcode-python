from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]

        stone = [0 for i in range(len(nums))]
        # 第一种
        stone[0] = nums[0]
        stone[1] = max(nums[0], nums[1])
        for i in range(2, length):
            stone[i] = max(stone[ i -2] + nums[i], stone[ i -1])
        return stone[-1]

    def rob_1(self, nums: List[int]) -> int:
        """
        考虑到每间房屋的最高总金额只和该房屋的前两间房屋的最高总金额相关，因此可以使用滚动数组，在每个时刻只需要存储前两间房屋的最高总金额。
        :param nums:
        :return:
        """
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        return second
