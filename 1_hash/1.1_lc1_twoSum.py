"""
题目链接：https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
"""

class Solution(object):
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i_index, i in enumerate(nums):
            for b_index, b in enumerate(nums):
                if i_index >= b_index:
                    continue
                if i + b == target:
                    return [i_index, b_index]

    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i_index, i in enumerate(nums):
            print(f"first:{i}")
            leave_list = nums[i_index + 1:]
            for b_index, b in enumerate(leave_list):
                print(f"second:{b}")
                # if i_index >= b_index:
                #     continue
                if i + b == target:
                    return [i_index, b_index + i_index + 1]

    def twoSum_3(self, nums, target):
        """
        最优
        :param nums:
        :param target:
        :return:
        """
        seen = {}
        for i, num in enumerate(nums):
            print(seen)
            complement = target - num
            if complement in seen:
                print(i, num)
                print('===')
                return [seen[complement], i]
            seen[num] = i

    def twoSum_4(self, nums, target):
        """
        会多一些资源的开销
        :param nums:
        :param target:
        :return:
        """
        seen = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            # seen[num] = i

    def twoSum_5(self, nums, target):
        # 保留原始索引
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # 按数值排序
        indexed_nums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []  # 题目保证有解，

    
if __name__ == "__main__":
    my = Solution()
    my_list = [3,2,4]
    my_target = 6
    # result = my.twoSum_2(my_list, my_target)
    # result = my.twoSum_3(my_list, my_target)
    # result = my.twoSum_4(my_list, my_target)
    result = my.twoSum_5(my_list, my_target)
    print(result)