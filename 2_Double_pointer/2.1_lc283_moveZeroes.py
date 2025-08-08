from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

def moveZeroes_1(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero_count = nums.count(0)
    nums[:] = [x for x in nums if x != 0] + [0] * zero_count

def moveZeroes_4(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zorro_list = []
    not_zorro_list = []
    for i in nums:
        if i == 0:
            zorro_list.append(i)
        else:
            not_zorro_list.append(i)
    nums[:len(not_zorro_list)] = not_zorro_list
    nums[len(not_zorro_list):] = zorro_list

def moveZeroes_3(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n == 1:
        return nums
    left = 0
    for i in range(n):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    nums[left:] = [0] * (n - left)


def moveZeroes_1(nums):
    left = 0  # 指向非零元素的插入位置
    for right in range(len(nums)):
        print(f"left:{left}, right:{right}")
        print(nums)
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]  # 调换位置
            print('===')
            left += 1
            

if __name__ == "__main__":
    nums = [20, 0, 0, 0, 1,0,3,12]
    # resp = moveZeroes_1(nums)
    resp = moveZeroes_2(nums)
    print(nums)
