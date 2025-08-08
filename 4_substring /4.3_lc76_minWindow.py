
from collections import defaultdict

def minWindow(s: str, t: str) -> str:
    """
    寻找s中包含t所有字符的最短子串
    方法一：滑动窗口
    参数:
        s: 源字符串
        t: 目标字符串

    返回:
        最小覆盖子串
    """
    if not s or not t or len(s) < len(t):
        return ""

    # 统计t中字符出现次数
    target_counts = defaultdict(int)
    for char in t:
        target_counts[char] += 1

    required = len(target_counts)  # 需要匹配的独特字符数量
    formed = 0  # 当前窗口中已匹配的独特字符数量
    window_counts = defaultdict(int)

    # 滑动窗口指针
    left = right = 0
    # 结果记录 (窗口长度, 左边界, 右边界)
    result = (float('inf'), None, None)

    while right < len(s):
        char = s[right]
        window_counts[char] += 1

        # 如果当前字符在t中，且数量匹配
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        # 尝试收缩左边界
        while left <= right and formed == required:
            # 更新最小窗口
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)

            # 移动左边界
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed -= 1
            left += 1

        right += 1

    return "" if result[0] == float('inf') else s[result[1]:result[2 ] +1]



def minWindow_optimized(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    target_counts = defaultdict(int)
    for char in t:
        target_counts[char] += 1

    required = len(target_counts)
    filtered_s = []

    # 预处理：只保留s中存在于t的字符及其索引
    for i, char in enumerate(s):
        if char in target_counts:
            filtered_s.append((i, char))

    left = formed = 0
    result = (float('inf'), None, None)
    window_counts = defaultdict(int)

    for right in range(len(filtered_s)):
        char = filtered_s[right][1]
        window_counts[char] += 1

        if window_counts[char] == target_counts[char]:
            formed += 1

        while left <= right and formed == required:
            start = filtered_s[left][0]
            end = filtered_s[right][0]

            if end - start + 1 < result[0]:
                result = (end - start + 1, start, end)

            left_char = filtered_s[left][1]
            window_counts[left_char] -= 1
            if window_counts[left_char] < target_counts[left_char]:
                formed -= 1
            left += 1

    return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    resp = minWindow(s, t)
    print(resp)