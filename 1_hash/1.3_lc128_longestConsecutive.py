import copy


class Solution(object):
    def longestConsecutive(self, nums):
        """leetcode官方解法"""
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:  # 是连续序列的起点
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longestConsecutive_1(self, nums):
        """
        正确
        :param nums:
        :return:
        """
        if not nums:
            return 0

        nums.sort()
        max_len = current_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_len += 1
            elif nums[i] != nums[i - 1]:  # 跳过重复数字
                current_len = 1
            max_len = max(max_len, current_len)
        return max_len

    def longestConsecutive_4(self, nums):
        boundary = {}
        max_len = 0
        for num in nums:
            if num not in boundary:
                left = boundary.get(num - 1, 0)
                right = boundary.get(num + 1, 0)
                current_len = left + right + 1
                boundary[num] = current_len
                boundary[num - left] = current_len  # 更新左边界
                boundary[num + right] = current_len  # 更新右边界
                max_len = max(max_len, current_len)
        return max_len


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    # nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [1,0,1,2]
    # nums = [1,1,2]
    # nums = [100,4,200,1,3,2,101]
    nums = [100, 4, 1, 3, 2, 101]
    a = Solution()
    # resp = a.longestConsecutive(nums)
    resp = a.longestConsecutive_1(nums)
    print(resp)
