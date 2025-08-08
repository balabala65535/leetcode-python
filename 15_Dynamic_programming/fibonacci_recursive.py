

def fibonacci_recursive(n: int) -> int:
    "递归实现（最直观，但效率最低）"
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 测试
print([fibonacci_recursive(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """
    记忆化递归（优化递归，避免重复计算）
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

# 测试
print([fibonacci_memo(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibonacci_iterative(n: int) -> int:
    """
    迭代实现（推荐，高效且节省内存）
    :param n:
    :return:
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b  # 状态更新
    return b

# 测试
print([fibonacci_iterative(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fibonacci_dp(n: int) -> int:
    """
    动态规划（类似迭代，但显式存储所有值）
    :param n:
    :return:
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 测试
print([fibonacci_dp(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibonacci_generator():
    """
    生成器实现（按需生成斐波那契数列）
    需要无限生成斐波那契数列
    节省内存（不存储所有值）
    :return:
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 测试
fib = fibonacci_generator()
print([next(fib) for _ in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
