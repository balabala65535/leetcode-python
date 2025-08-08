from typing import *


class Solution1:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0  # maxPos 可到达的最远位置
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                print(i, end ,maxPos)
                if i == end:
                    print('----')
                    end = maxPos
                    step += 1
        return step



class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        方法一：反向查找出发位置
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

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
