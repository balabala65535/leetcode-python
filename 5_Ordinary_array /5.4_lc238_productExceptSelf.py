
def productExceptSelf(nums):
    """
    我-左右乘积列表：21%&34%
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    left_multiply = [nums[0]]
    for i in range(1, length):
        left_multiply.append(nums[i] * left_multiply[i-1])

    right_multiply = [0] * length
    right_multiply[-1] = nums[-1]
    current_index = length - 1 - 1
    while current_index >= 0:
        right_multiply[current_index] = nums[current_index] * right_multiply[current_index + 1]
        current_index -= 1

    result_list = []
    for i in range(length):
        if i > 0:
            left_value = left_multiply[i - 1]
        else:
            left_value = 1
        if i < length - 1:
            right_value = right_multiply[i + 1]
        else:
            right_value = 1

        result_list.append(left_value * right_value)
    return result_list



def productExceptSelf_2(nums):
    """

    :param nums:
    :return:
    """
    length = len(nums)
    total = 1
    for i in range(length):
        if nums[i] != 0:
            total *= nums[i]
    result_list = []
    for i in range(length):
        if nums[i] != 0:
            result_list.append(total/nums[i])
        else:
            result_list.append(0)

    return result_list


def productExceptSelf_3(nums):
    """
    官方--87%&75%
    :param nums:
    :return:
    """
    length = len(nums)
    answer = [0] * length

    # answer[i] 表示索引 i 左侧所有元素的乘积
    # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    # R 为右侧所有元素的乘积
    # 刚开始右边没有元素，所以 R = 1
    R = 1
    for i in reversed(range(length)):
        # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
        answer[i] = answer[i] * R
        # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
        R *= nums[i]

    return answer

def productExceptSelf_4(nums):
    """
    官方-左右乘积列表-87%&75%
    :param nums:
    :return:
    """
    length = len(nums)

    # L 和 R 分别表示左右两侧的乘积列表
    L, R, answer = [0] * length, [0] * length, [0] * length

    # L[i] 为索引 i 左侧所有元素的乘积
    # 对于索引为 '0' 的元素，因为左侧没有元素，所以 L[0] = 1
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i - 1] * L[i - 1]

    # R[i] 为索引 i 右侧所有元素的乘积
    # 对于索引为 'length-1' 的元素，因为右侧没有元素，所以 R[length-1] = 1
    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        R[i] = nums[i + 1] * R[i + 1]

    # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
    for i in range(length):
        answer[i] = L[i] * R[i]

    return answer



if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    nums = [-1,1,0,-3,3]
    resp = productExceptSelf_3(nums)
    print(resp)

