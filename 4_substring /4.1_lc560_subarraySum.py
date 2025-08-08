

def subarraySum_1(nums, k):
    """
    以 i 结尾和为 k 的连续子数组个数，我们需要统计符合条件的下标 j 的个数，其中 0≤j≤i 且 [j..i] 这个子数组的和恰好为 k
    方法一：枚举---运行超时

    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    for start in range(len(nums)):
        sum = 0
        end = start
        while end >= 0:
            sum += nums[end]
            end -= 1
            if sum == k:
                count += 1
    return count


def subarraySum_2(nums, k):
    """
    |--(pre - k)---|---K---| = pre
    :param nums:
    :param k:
    :return:
    """
    count = 0
    pre = 0
    m = {}
    m[0] = 1
    for i in range(len(nums)):
        pre += nums[i]
        if pre - k in m:
            count += m[pre - k]
        m.setdefault(pre, 0)
        m[pre] += 1
        print(m)
    return count




if __name__ == "__main__":
    # nums = [1,1,1,2,3,3,4,4,5]
    # nums = [1,2,3,1,1,2,3]
    # nums = [1,1,1]
    nums = [1,-1,0]
    # k = 4
    # k = 3
    k = 0
    # resp = subarraySum(nums, k)
    # resp = subarraySum_1(nums, k)
    resp = subarraySum_2(nums, k)
    print(resp)