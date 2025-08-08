from typing import *


class Solution:
    def my_longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_1 = len(text1)
        max_sub_length = 0
        for i in range(1, length_1):
            for j in range(i):
                if text1[j:i] in text2:
                    max_sub_length = max(max_sub_length, i - j +1)
        return max_sub_length

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if i == 2 and j == 5:
                    print('i == 2 and j == 5', dp[i][j])

        return dp[m][n]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"

    text1 = "bdcaba"
    text2 = "abcbdab"

    a = Solution()
    resp = a.longestCommonSubsequence(text1, text2)
    print(resp)