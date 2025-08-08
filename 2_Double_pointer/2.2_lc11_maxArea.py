
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    暴力解法
    """
    max_area = 0
    height_length = len(height)
    for my_index in range(height_length):
        for next_index in range(my_index+1, height_length):
            my_area = abs((next_index - my_index) * min(height[my_index], height[next_index]))
            max_area = max(max_area, my_area)
    return max_area


def maxArea_1(height):
    """
    :type height: List[int]
    :rtype: int
    双指针--- 需要左右移动的一般用双指针
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        my_area = abs((right - left) * min(height[left], height[right]))
        max_area = max(max_area, my_area)
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    # resp = maxArea(height)
    resp = maxArea_1(height)
    print(resp)