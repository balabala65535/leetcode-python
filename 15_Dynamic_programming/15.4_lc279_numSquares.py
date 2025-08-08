




import math

def numSquares(n):
    """
    为什么是 dp[i - j*j] + 1？
    dp[i - j*j]
    表示去掉一个完全平方数 j*j 后剩下的数字 i - j*j 的最少平方数个数。
    例如：
    如果 i = 5，j = 2（即 j*j = 4），则 i - j*j = 1，而 dp[1] = 1。
    这意味着 5 = 4 + 1，总共需要 dp[1] + 1 = 2 个平方数（4 和 1）。
    + 1
    表示当前选择的这个 j*j 也算作一个平方数，所以要加 1。
    =====
    # 初始化dp数组，dp[i]表示和为i的完全平方数的最少数量
    # dp[i] 表示数字 i 最少可以由多少个完全平方数相加得到。


    :param n:
    :return:
    """

    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 边界条件
    print(dp)
    # 预计算所有可能的完全平方数
    max_square = int(math.isqrt(n)) + 1
    # max_square = 3
    square_nums = [i*i for i in range(1, max_square)]

    for i in range(1, n + 1):
        for square in square_nums:
            # print(square)
            if square > i:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)
    print(dp)
    return dp[n]

# 测试
print(numSquares(4))  # 输出: 3 (4 + 4 + 4)
# print(numSquares(13))  # 输出: 2 (4 + 9)


def numSquares(n):
    """
    优化的动态规划（减少内层循环）
    :param n:
    :return:
    """
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:  #  1, 4, 9, 16
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    print(dp)
    return dp[n]


import math

def numSquares(n: int) -> int:
    """
    方法4：生成完全平方数序列
    :param n:
    :return:
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = min((dp[i - j * j] for j in range(1, int(math.isqrt(i)) + 1)), default=0) + 1
    return dp[n]


import math


def numSquares(n):
    """
    数学解法（基于四平方和定理，时间复杂度 O(√n)）
    :param n:
    :return:
    """
    # 检查是否是完全平方数
    def is_perfect_square(x):
        s = int(math.isqrt(x))
        return s * s == x

    # 检查是否符合四平方和定理的条件
    if is_perfect_square(n):
        return 1

    # 检查是否可以表示为4^k*(8m+7)形式
    temp = n
    while temp % 4 == 0:
        temp //= 4
    if temp % 8 == 7:
        return 4

    # 检查是否可以表示为两个平方数之和
    for i in range(1, int(math.isqrt(n)) + 1):
        if is_perfect_square(n - i * i):
            return 2

    # 其他情况返回3
    return 3


# 测试
print(numSquares(12))  # 3
print(numSquares(13))  # 2
print(numSquares(7))  # 4 (4 + 1 + 1 + 1)