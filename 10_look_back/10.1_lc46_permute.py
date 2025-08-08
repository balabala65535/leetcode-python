
"""
回溯法：一种通过探索所有可能的候选解来找出所有的解的算法。如果候选解被确认不是一个解（或者至少不是最后一个解），
回溯算法会通过在上一步进行一些变化抛弃该解，即回溯并且再次尝试。

def backtrack(path, choices):
    if 满足条件:
        记录结果
        return
    for 选择 in choices:
        做选择
        backtrack(path, new_choices)  # 递归
        撤销选择

关键点：
排列问题必须用 递归回溯 或 Heap's Algorithm（非递归版）。
避免频繁 copy 和 insert，改用 交换 + 回溯 提升效率。
"""

def permute(nums):
    """

    :param nums:
    :return:
    """
    import copy
    length = len(nums)
    result = [nums]
    for i in range(length):
        for i1 in range(1, length):
            new = copy.deepcopy(nums)
            cur_val = new.pop(i)
            insert_index = (i + i1) % length
            new.insert(insert_index, cur_val)
            result.append(new)
    return result


def permute(nums):
    def backtrack(first=0):
        print('==========', first, '==========')
        if first == len(nums):
            result.append(nums.copy())  # 记录当前排列
            return
        for i in range(first, len(nums)):
            print(nums)
            nums[first], nums[i] = nums[i], nums[first]  # 交换
            backtrack(first + 1)  # 递归下一层
            print("*****")
            nums[first], nums[i] = nums[i], nums[first]  # 撤销交换
            print(nums)
        print("-------"*3)
    result = []
    backtrack()
    return result

if __name__ == "__main__":
    nums = [1,2,3]
    resp = permute(nums)
    for i in resp:
        print(i)

