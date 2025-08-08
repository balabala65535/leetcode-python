
def lengthOfLongestSubstring(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):

        if i != 0:
            # 左指针向右移动一格，移除一个字符
            print('左指针向右移动一格，移除一个字符')
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:  # 但凡发现一个在就终止循环了
            # 不断地移动右指针
            occ.add(s[rk + 1])
            print(rk+1, occ)
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
        print("------")
    return ans

def lengthOfLongestSubstring_1(s: str) -> int:
    """
    使用堆栈的方法
    :param s:
    :return:
    """
    from collections import deque
    my_deque = deque()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i > 0:
            my_deque.popleft()
        while rk + 1 < n and s[rk + 1] not in my_deque:
            my_deque.append(s[rk + 1])
            rk += 1
            ans = max(ans, len(my_deque))
            print(my_deque)
    return ans


def lengthOfLongestSubstring_2(s: str) -> int:
    """
    1.不含有重复字符的子串
    2.求出长度
    :param s:
    :return:
    """
    my_max = []
    matched_str = ''
    max_length = 0
    for my_index, i in enumerate(s):
        if i in s[my_index + 1:]:
            matched_str += i
        else:
            print(matched_str)
            max_length = max(max_length, len(matched_str))
            matched_str = ''
    return max_length


if __name__ == "__main__":
    s = "aaeabcabcbbe"
    # s = "bbbbb"
    # s = "pwwkew"
    # resp = lengthOfLongestSubstring(s)
    # print(resp)
    # resp = lengthOfLongestSubstring_1(s)
    resp = lengthOfLongestSubstring_2(s)
    print(resp)