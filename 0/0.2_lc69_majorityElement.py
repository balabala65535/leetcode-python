
def majorityElement(nums):
    """
    方法一：哈希表计数法
    O(n) & O(n)
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num



def majorityElement_1(nums):
    """
    方法二：排序法
    时间复杂度：O(n log n)
    空间复杂度：O(1) 或 O(n)（取决于排序实现）
    :param nums:
    :return:
    """

    nums.sort()
    return nums[len(nums)//2]


def majorityElement_2(nums):
    """
    方法三：Boyer-Moore投票算法（最优解）
    :param nums:
    :return:
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


def majorityElement_4(nums):
    """
    时间复杂度：O(n log n)
    空间复杂度：O(log n)（递归栈空间）
    :param nums:
    :return:
    """
    def majority_element_rec(lo, hi):
        # 基本情况：单个元素就是多数元素
        if lo == hi:
            return nums[lo]

        # 分治递归
        mid = (hi - lo) // 2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid + 1, hi)

        # 如果两边的多数元素相同，直接返回
        if left == right:
            return left

        # 否则统计在整个区间内哪个出现次数更多
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)