from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        反向查找出发位置
        :param nums:
        :return:
        """
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps

    def jump_1(self, nums: List[int]) -> int:
        """
        正向查找可到达的最大位置
        :param nums:
        :return:
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0  # maxPos 可到达的最远位置
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

