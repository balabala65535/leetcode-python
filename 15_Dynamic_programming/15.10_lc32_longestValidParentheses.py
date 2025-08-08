

def longestValidParentheses(s: str) -> int:
    """
    方法 1：动态规划（DP）
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * n
    max_len = 0
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0)
            max_len = max(max_len, dp[i])
    return max_len


def longestValidParentheses(s: str) -> int:
    """
    方法 2：栈（Stack）
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    stack = [-1]  # 初始化栈底
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # 更新边界
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len


def longestValidParentheses(s: str) -> int:
    """
    方法 3：双指针（空间优化）
    时间复杂度：O(n)
    空间复杂度：O(1)
    :param s:
    :return:
    """
    left = right = max_len = 0
    n = len(s)
    # 从左到右扫描
    for i in range(n):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0
    # 从右到左扫描
    left = right = 0
    for i in range(n-1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0
    return max_len
