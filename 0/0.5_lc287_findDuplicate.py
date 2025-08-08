
"""
实际应用
数据库去重：快速找出重复记录
网络数据校验：检测重复传输的数据包
资源分配：确保没有重复分配的资源ID
基因组学：寻找DNA序列中的重复片段

龟兔赛跑：慢指针（龟）每次走1步，快指针（兔）每次走2步
必然相遇：因为兔比龟快，在圆形跑道上一定会追上龟
重复数就是跑道入口：相遇后，从起点和相遇点同时出发，再次相遇的位置就是重复数字；
现在你应该完全理解这个巧妙的算法了！它把数组索引和值的关系转化为链表问题，再利用快慢指针的精妙数学原理找到解，确实是这类问题的最优解法。

为什么这能找出重复数？
数组构成隐式链表：把数组值看作指针（nums[i]指向nums[nums[i]]）
重复数必然形成环：因为至少有两个索引指向同一个值
龟兔相遇原理：
快指针速度是慢指针的2倍
在环内快指针最终会追上慢指针
入口即重复数：
数学证明：从起点到环入口的距离 = 相遇点到环入口的距离
所以两个指针同速前进必然在入口处相遇
Q2：如果数组有多个重复数怎么办？
A2：这个算法只适用于恰好一个重复数的情况。多个重复数需要用其他方法。
"""
from typing import *



class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    def findDuplicate_2(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicate_3(self, nums):
        """
        a=(k−1)L+(L−b)=(k−1)L+c
        :param nums:
        :return:
        """
        # 第一阶段：找到相遇点
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                break

        # 第二阶段：找到环的入口（重复数）
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

    def findDuplicate_4(self, nums):
        left, right = 1, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left

    def findDuplicate_5(self, nums):
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()

        for bit in range(bits):
            mask = 1 << bit
            expected = actual = 0

            for i in range(n + 1):
                # 计算1到n的位统计
                if i & mask:
                    expected += 1
                # 计算数组中数字的位统计
                if nums[i] & mask:
                    actual += 1

            if actual > expected:
                duplicate |= mask

        return duplicate

    def findAllDuplicates(self, nums):
        """
        扩展：多个重复数的情况
        如果需要找出所有重复数（假设有多个重复数）：

        数字范围保证：题目给定数字范围是1 ≤ a[i] ≤ n（n=数组长度）
        所以 abs(num)-1 一定是有效索引
        符号标记法：
        第一次遇到数字x时，将 nums[x-1] 设为负数
        如果再次遇到x，发现 nums[x-1] 已经是负数，说明x是重复的
        不破坏原始信息：
        使用绝对值 abs(num) 获取原始值
        只修改符号位，不影响数值的绝对值
        """
        res = []
        for num in nums:

            index = abs(num) - 1
            print(num, f'={index}==>', nums)
            if nums[index] < 0:
                print(';lalal', nums[index])
                res.append(abs(num))
            nums[index] = -nums[index]
        return res


if __name__ == "__main__":
    # nums = [4,5,2,6,3,1]
    # nums = [4, 2, 1, 2, 3, 5, 6, 1]
    nums = [3,3,3,3]
    a = Solution()
    # resp = a.nextPermutation(nums)
    # resp = a.findDuplicate_3(nums)
    resp = a.findAllDuplicates(nums)
    print(resp)
