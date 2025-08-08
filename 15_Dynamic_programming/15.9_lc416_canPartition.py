from typing import *



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        这行代码常见于动态规划（DP）问题中，特别是涉及布尔状态转移的情况（如背包问题、子集和问题等）。它的作用是：
        如果 dp[j - num] 为 True，则 dp[j] 也设为 True，表示当前状态 j 可以通过某种方式达到。

        2. dp[j] |= dp[j - num]（按位或赋值）
        保留历史状态：相当于 dp[j] = dp[j] or dp[j - num]。

        如果 dp[j] 原本为 True，无论 dp[j - num] 是 True 还是 False，dp[j] 仍为 True。

        只有 dp[j] 原本为 False 且 dp[j - num] 为 True 时，dp[j] 才会被设为 True。

        不会丢失信息：确保所有可能的组合都被考虑。

        """
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]


