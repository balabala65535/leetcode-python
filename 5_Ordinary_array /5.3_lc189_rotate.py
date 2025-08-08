import copy


def rotate(nums, k):
    """
    击败100% & 72%
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    k = k % length
    k_list = nums[length - k:]
    new_nums = k_list + nums[:length - k]
    nums[:] = new_nums


def rotate_1(nums, k):
    """
    55% & 84%
    :param nums:
    :param k:
    :return:
    """
    length = len(nums)
    k = k % length
    k_list = nums[length - k:]
    for i in nums[0: length - k]:
        k_list.append(i)
    nums[:] = k_list
    return nums


def rotate_2(nums, k):
    """
    击败5% &5%
    :param nums:
    :param k:
    :return:
    """
    org_nums = copy.deepcopy(nums)
    length = len(nums)
    k = k % length
    for i in range(k):
        nums[i] = org_nums[length - k + i]
    # 后面
    for i in range(k, length):
        nums[i] = org_nums[i - k]
    return nums


def rotate_4(nums, k):
    """
    官方解法：使用额外的数组
    20%&25%
    :param nums:
    :param k:
    :return:
    """
    length = len(nums)
    new_nums = [0] * length
    for i, v in enumerate(nums):
        new_nums[(i + k) % length] = v
    nums[:] = new_nums
    return new_nums


def rotate_5(nums, k):
    """
    官方解法：环状替换--- 没懂
    20%&25%
    :param nums:
    :param k:
    :return:
    """

    def gcd(a, b):
        if a != 0:
            a, b = b % a, a
        return b

    n = len(nums)
    k = k % n
    start, count = 0, gcd(k, n)
    while start < count:
        pre, cur = nums[start], start
        count += 1
        ok = True
        while ok:
            next = (cur + k) % n
            nums[next], pre, cur = pre, nums[next], next
            ok = cur != start
            print(ok)


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3

    # nums = [-1]
    # k = 2
    #
    # nums = [1, 2]
    # k = 5

    resp = rotate_5(nums, k)
    print(nums)
    print(resp)