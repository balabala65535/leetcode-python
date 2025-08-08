
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    all_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        print(f"{left}&{right}")
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            print(f"{left}&{right}")
            all_area += abs((right-left)*2*height[left])
            # 判断哪些数据在这个范围里
            dup_area = len([i for i in height if i <= height[left]]) * height[left]
            all_area -= dup_area
            left += 1
            right -= 1
    return all_area


def trap_1(height):
    """
    一列一列的算,直觉算法
    :param height:
    :return:
    """
    height_num = len(height)
    dup_area = 0
    for i in range(1, height_num - 1):
        # 计算每列的水深
        max_left = max([height[i] for i in range(0, i)])
        max_right = max([height[i] for i in range(i+1, height_num)])
        max_deep = min([max_left, max_right])
        # print(i, height[i],  max_deep)
        if max_deep > height[i]:
            dup_area += max_deep - height[i]
    return dup_area

def trap_2(height):
    """
    动态规划算法
    :param height:
    :return:
    """
    # 求从做到右最大的max
    left_max = []
    tmp_max = 0
    for i in height:
        tmp_max = max([i, tmp_max])
        left_max.append(tmp_max)
    # 求右到左的最大max
    right_max = []
    tmp_max = 0
    for i in height[::-1]:
        tmp_max = max([i, tmp_max])
        right_max.append(tmp_max)
    new_right_nax = right_max[::-1]
    drop_area = sum([min([left_max[i], new_right_nax[i]]) - height[i] for i in range(len(height))])
    return drop_area


def trap_3(height) -> int:
    """
    单调栈
    :param height:
    :return:
    """
    ans = 0
    stack = list()  # 存储未算面积的index

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:  # 若比前面柱子更高时进入循环，否则直接添加
            top = stack.pop()  # 移除列表中的最后一个元素，并将移除出的元素赋予变量top
            if not stack:
                break
            left = stack[-1]
            currWidth = i - left - 1
            currHeight = min(height[left], height[i]) - height[top]
            ans += currWidth * currHeight
        # 将当前元素的index加入栈
        stack.append(i)
        print(stack)
    return ans


def trap_4(height) -> int:
    """
    双指针
    :param height:
    :return:
    """
    ans = 0
    left, right = 0, len(height) - 1
    leftMax = rightMax = 0

    while left < right:
        leftMax = max(leftMax, height[left])
        rightMax = max(rightMax, height[right])
        if height[left] < height[right]:
            ans += leftMax - height[left]
            left += 1
        else:
            ans += rightMax - height[right]
            right -= 1

    return ans



if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [4,2,0,3,2,5]
    # height = [0]*4
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # resp = trap(height)
    # resp = trap_1(height)
    resp = trap_3(height)
    print(resp)

