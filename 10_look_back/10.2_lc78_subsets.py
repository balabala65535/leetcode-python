import copy


def subsets(nums):
    ...

    def backtrack(first=0):
        # if first <= len(new_nums):
        #     result.append(new_nums.copy())
        #     # return
        for i in range(first + 1, len(nums)):
            result.append(nums[first:i])
            # print(nums)
            # # nums[first], nums[i] = nums[i], nums[first]  # 交换
            backtrack(first + 1)  # 递归下一层
            # print("*****")
            # nums[first], nums[i] = nums[i], nums[first]  # 撤销交换

    result = [[]]
    backtrack()
    return result


def subsets_1(nums):
    res = [[]]
    for i in range(len(nums)):
        for j in range(len(res)):
            res.append(res[j] + [nums[i]])
    return res


def subsets_2(nums):
    n = len(nums)
    return [[nums[i] for i in range(n) if (mask >> i) & 1] for mask in range(1 << n)]


def subsets_3(nums):
    n = len(nums)
    ans = []
    for mask in range(1 << n):  # 1<<n 等于 2^n
        print(mask)
        subset = []
        for i in range(n):
            if (mask >> i) & 1:  # 检查第 i 位是否为 1
                subset.append(nums[i])
        ans.append(subset.copy())  # 避免引用问题
    return ans


def subsets_11(nums):
    """
    递归回溯法（DFS）
    :param nums:
    :return:
    """

    def backtrack(start, path):
        print("我开始了。。。。", start, '   |||   ', path)
        res.append(path.copy())  # 添加当前子集
        for i in range(start, len(nums)):
            path.append(nums[i])  # 选择当前元素
            print('1==>', path)
            backtrack(i + 1, path)  # 递归下一层
            a = path.pop()  # 撤销选择
            print('2==>', path)

    res = []
    backtrack(0, [])
    return res


def subsets_my11(nums):
    result = []
    son_set = []

    def backtrack(my_nums, my_index=0):
        result.append(son_set.copy())
        if len(my_nums) <= my_index:
            return
        for i in range(my_index, len(my_nums)):
            son_set.append(my_nums[i])
            backtrack(my_nums, i + 1)
            son_set.pop()

    backtrack(nums, 0)
    return result


def subsets_12(nums):
    res = [[]]
    for num in nums:
        res += [subset + [num] for subset in res]
    return res


def subsets_13(nums):
    from itertools import combinations
    res = []
    for i in range(len(nums) + 1):
        res += list(combinations(nums, i))
    return [list(x) for x in res]


def subsets_14(nums):
    res = []
    n = len(nums)
    for mask in range(1 << n):
        res.append([nums[i] for i in range(n) if (mask >> i) & 1])
    return res


def subset_my(nums):
    result = [[]]
    son_set = []

    def backtrack(my_nums, start_index=0):
        if len(my_nums) >= start_index:
            result.append(my_nums)
            return
        for i in range(start_index, len(my_nums)):
            son_set.append(my_nums[i])
            backtrack(son_set, i + 1)
            son_set.pop()

    backtrack(nums, 0)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    # resp = subsets_11(nums)
    resp = subsets_3(nums)
    for i in resp:
        print(i)
