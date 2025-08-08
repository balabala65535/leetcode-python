from typing import *


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j]
                down = D[i][j - 1]
                left_down = D[i - 1][j - 1]
                # if word1[i - 1] == word2[j - 1]:
                #     left_down -= 1
                # D[i][j] = 1 + min(left, down, left_down)
                if word1[i - 1] == word2[j - 1]:
                    D[i][j] = left_down
                else:
                    D[i][j] = 1 + min(left, down, left_down)


        return D[n][m]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    a = Solution()
    resp = a.minDistance(word1, word2)
    print(resp)