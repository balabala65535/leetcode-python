
class Solution:
    def partition(self, s: str):
        # 判断子串是否为回文字符串
        """
        单个字符的子串（i == j）必定是回文串，所以对角线f[i][i]初始为True
        其他位置初始值会被后续计算覆盖
        [[T, F, F, T],  # "a", "ab", "abb", "abba"
         [ , T, T, F],  # "b", "bb", "bba"
         [ ,  , T, F],   # "b", "ba"
         [ ,  ,  , T]     # "a"]
        :param s:
        :return:
        """
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                print(i, j)
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]  # 首尾字符串相同，且去掉首尾字符串后也是回文字符串

        ret = list()
        ans = list()
        for i in f:
            print(i)
        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i: j +1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return ret

if __name__ == "__main__":
    # s = "aab"
    s = "abba"
    resp = Solution().partition(s)
    print(resp)