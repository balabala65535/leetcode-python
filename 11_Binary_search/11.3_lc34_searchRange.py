
import bisect
from typing import *

def searchRange(nums, target):
    leftmost = bisect.bisect_left(nums, target)
    if leftmost == len(nums) or nums[leftmost] != target:
        return [-1, -1]

    rightmost = bisect.bisect_right(nums, target) - 1
    return [leftmost, rightmost]


def searchRange(nums, target):
    def find_left():
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def find_right():
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l - 1

    left = find_left()
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, find_right()]


def searchRange(nums, target):
    """
    最好，100% & 11%
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return [-1, -1]

    l, r = 0, len(nums) - 1
    # 先找左边界
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    if nums[l] != target:
        return [-1, -1]

    left = l
    r = len(nums) - 1
    # 再找右边界
    while l < r:
        mid = (l + r + 1) // 2  # 向上取整避免死循环
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid

    return [left, r]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        错误，不能覆盖[2,2]，target 2场景
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1
        target_left = target_right = -1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                target_left = min(target_left, mid) if target_left != -1 else mid
                target_right = max(target_right, mid)
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return [target_left, target_right]
