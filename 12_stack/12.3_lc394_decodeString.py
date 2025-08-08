

class Solution:
    def decodeString(self, s: str) -> str:
        """栈操作"""
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)  # 为了防止"100[leetcode]" 这种情况
            else:
                res += c
        return res

    def decodeString_1(self, s: str) -> str:
        """递归"""
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)

    def decodeString_2(self, s: str) -> str:
        lt = []
        num = ""
        for i in range(len(s)):
            print(lt)
            if ord("0") <= ord(s[i]) <= ord("9"):
                num += s[i]
            else:
                if num:
                    lt.append(num)
                    num = ""
                if s[i] == "]":
                    str = ""
                    while lt[-1] != "[":
                        str = lt.pop() + str
                    lt.pop()  # 去掉[
                    str = str * int(lt.pop())
                    lt.append(str)
                else:
                    lt.append(s[i])
        return "".join(lt)

if __name__ == "__main__":
    s = "3[a2[c]]"
    a = Solution()
    resp = a.decodeString_2(s)
    print(resp)