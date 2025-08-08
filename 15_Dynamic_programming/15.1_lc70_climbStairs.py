


def climb_stairs(n: int) -> int:
    """
    100%&74%， 自底向上迭代（推荐）
    :param n:
    :return:
    """
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2  # 初始条件
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 状态转移
    return dp[n]

# 测试
print(climb_stairs(5))  # 输出：8（共有8种方法爬到第5阶）


def climb_stairs(n: int) -> int:
    """
    100%&74%， 优化空间复杂度o(1)
    :param n:
    :return:
    """
    if n <= 2:
        return n
    a, b = 1, 2  # a=dp[i-2], b=dp[i-1]
    for _ in range(3, n + 1):
        a, b = b, a + b  # 状态转移
    return b

# 测试
print(climb_stairs(5))  # 输出：8

def climb_stairs_3(n: int) -> int:
    """
    100%&74%， 优化空间复杂度o(1)
    :param n:
    :return:
    """
    if n <= 2:
        return n
    a, b = 1, 2  # a=dp[i-2], b=dp[i-1]
    for _ in range(3, n + 1):
        a, b = b, a + b  # 状态转移
    return b