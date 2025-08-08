def findAnagrams_my(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    match_index = []
    tmp_match_index = []

    matched_str = {}
    need_str = {i: p.count(i) for i in p}
    for my_index, i in enumerate(s):
        if i in p and i not in matched_str:
            matched_str[i] = 1
            tmp_match_index.append(my_index)
        elif i in need_str and i in need_str:
            if need_str[i] <= matched_str[i]:
                # 元素中断了归零，重找
                matched_str = {}
                tmp_match_index = []
                matched_str[i] = 1
                tmp_match_index.append(my_index)
            else:
                matched_str[i] += 1
                tmp_match_index.append(my_index)
        elif i not in need_str:
            # 元素中断了归零，重找
            matched_str = {}
            tmp_match_index = []

        # 检查满足了没
        if need_str == matched_str:
            match_index.append(tmp_match_index[0])
            tmp_match_index = []
            matched_str = {}
            if i in p and i not in matched_str:
                matched_str[i] = 1
                tmp_match_index.append(my_index)

    return match_index


def findAnagrams_1(s, p):
    """
    此解法会超时
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    match_index = []
    p_length = len(p)
    need_str = {i: p.count(i) for i in p}
    for my_index, i in enumerate(s):
        # 往后找对应长度的字符串
        now_str = s[my_index: my_index + p_length]
        str_dict = {i: now_str.count(i) for i in now_str}
        if str_dict == need_str:
            match_index.append(my_index)
    return match_index


def findAnagrams_2(s: str, p: str):
    """
    滑动窗口-官方
    """
    s_len, p_len = len(s), len(p)

    if s_len < p_len:
        return []

    ans = []
    s_count = [0] * 26
    p_count = [0] * 26
    for i in range(p_len):
        s_count[ord(s[i]) - 97] += 1
        p_count[ord(p[i]) - 97] += 1

    if s_count == p_count:
        ans.append(0)

    for i in range(s_len - p_len):
        s_count[ord(s[i]) - 97] -= 1
        s_count[ord(s[i + p_len]) - 97] += 1

        if s_count == p_count:
            ans.append(i + 1)

    return ans


def findAnagrams_3(s: str, p: str):
    s_len, p_len = len(s), len(p)

    if s_len < p_len:
        return []

    ans = []
    count = [0] * 26
    for i in range(p_len):
        count[ord(s[i]) - 97] += 1
        count[ord(p[i]) - 97] -= 1

    differ = [c != 0 for c in count].count(True)

    if differ == 0:
        ans.append(0)

    for i in range(s_len - p_len):
        if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
            differ -= 1
        elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
            differ += 1
        count[ord(s[i]) - 97] -= 1

        if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
            differ -= 1
        elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
            differ += 1
        count[ord(s[i + p_len]) - 97] += 1

        if differ == 0:
            ans.append(i + 1)
    return ans

from typing import *
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        length_p = len(p)
        p_count = defaultdict(int)
        window_count = defaultdict(int)

        # 初始化p的字符计数和第一个窗口的字符计数
        for i in range(length_p):
            p_count[p[i]] += 1
            window_count[s[i]] += 1

        result = []
        if window_count == p_count:
            result.append(0)
        print(p_count)
        # 滑动窗口
        for i in range(length_p, len(s)):
            # 移除左边界的字符
            left_char = s[i - length_p]
            if window_count[left_char] == 1:
                print("****", left_char, window_count[left_char])
                window_count[left_char] -= 1
                # del window_count[left_char]
            else:
                print(window_count)
                window_count[left_char] -= 1
                print('====', window_count)

            # 添加右边界的字符
            right_char = s[i]
            window_count[right_char] += 1

            # 比较当前窗口和p的字符计数
            if window_count == p_count:
                result.append(i - length_p + 1)

        return result



if __name__ == "__main__":
    s = "cbbaebabbacabcbd"
    p = "abbc"
    s = "abab"
    p = 'ab'
    # resp = findAnagrams_my(s, p)
    resp = findAnagrams_1(s, p)
    print('###', resp)
