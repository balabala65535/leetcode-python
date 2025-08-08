from typing import *
"""
实现获取"下一个排列"的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

实际应用场景
下一个排列算法可用于：

密码破解中的排列尝试

组合优化问题

游戏中的关卡排列

数据加密中的密钥生成

"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        首先从后向前查找第一个顺序对 (i,i+1)，满足 a[i]<a[i+1]。这样「较小数」即为 a[i]。此时 [i+1,n) 必然是下降序列。

        如果找到了顺序对，那么在区间 [i+1,n) 中从后向前查找第一个元素 j 满足 a[i]<a[j]。这样「较大数」即为 a[j]。

        交换 a[i] 与 a[j]，此时可以证明区间 [i+1,n) 必为降序。我们可以直接使用双指针反转区间 [i+1,n) 使其变为升序，而无需对该区间进行排序。

        """

        # 从后向前找较小数
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # 降序
            i -= 1
        if i >= 0:
            # 从后向前找比较小数，大的较大数。
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            print(nums[i], nums[j])
            nums[i], nums[j] = nums[j], nums[i]
        # print(nums[i], nums[j])
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def nextPermutation_2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # 第一步：从后向前查找第一个非递增的元素
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找到这样的元素
        if i >= 0:
            # 第二步：从后向前查找第一个大于nums[i]的元素
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 交换这两个元素
            nums[i], nums[j] = nums[j], nums[i]

        # 第三步：反转i+1到末尾的部分
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def permute(self, nums):
        """
        变种问题
        如果需要生成所有排列，可以使用回溯法：
        """
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

if __name__ == "__main__":
    # nums = [4,5,2,6,3,1]
    # nums = [1, 2, 3, 4, 5, 6]
    nums = [6,5,4,3,2,1]
    a = Solution()
    # resp = a.nextPermutation(nums)
    resp = a.permute(nums)
    print(resp)
    print(nums)
    for i in resp:
        print(i)
