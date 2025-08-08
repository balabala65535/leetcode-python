from typing import *

def My_wordBreak(s: str, wordDict: List[str]) -> bool:
    length = len(s)
    match_result = [False] * length
    scaned = ''
    for i in range(length):
        scaned += s[i]
        if scaned in wordDict:
            match_result[i] = True
            print(scaned)
            scaned = ''
    return match_result[-1]

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    word_set = set(wordDict)  # 转换为集合提高查找效率
    n = len(s)
    dp = [False] * (n + 1)    # dp[i]表示s的前i个字符能否被拆分
    dp[0] = True              # 空字符串可以被拆分

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]


def wordBreak_1(s, wordDict):
    word_set = set(wordDict)
    memo = {}

    def helper(s):
        if s in memo:
            return memo[s]
        if s in word_set:
            memo[s] = True
            return True

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in word_set and helper(s[i:]):
                memo[s] = True
                return True

        memo[s] = False
        return False

    return helper(s)


def wordBreakAll(s, wordDict):
    """
    变种问题：返回所有可能的拆分方式
    如果需要返回所有可能的拆分方式而不仅仅是判断能否拆分：
    :param s:
    :param wordDict:
    :return:
    """
    word_set = set(wordDict)
    memo = {}

    def helper(s):
        if s in memo:
            return memo[s]
        if not s:
            return [""]

        res = []
        for word in word_set:
            if s.startswith(word):
                sub_results = helper(s[len(word):])
                for sub in sub_results:
                    res.append(word + (" " + sub if sub else ""))
        memo[s] = res
        return res

    return helper(s)

if __name__ == "__main__":
    ...