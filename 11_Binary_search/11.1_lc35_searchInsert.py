def searchInsert(nums, target: int) -> int:
    """
    o(n) 100%&
    :param nums:
    :param target:
    :return:
    """
    start = nums[0]
    end = nums[-1]
    if target < start:
        return 0
    if end < target:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] >= target:
            return i


def searchInsert_1(nums, target):
    """
    100% & 60%
    :param nums:
    :param target:
    :return:
    """
    n = len(nums)
    left, right = 0, n - 1
    ans = n  # 默认插入位置在末尾

    while left <= right:
        mid = (right - left) // 2 + left  # 防止整型溢出的写法
        if target <= nums[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans