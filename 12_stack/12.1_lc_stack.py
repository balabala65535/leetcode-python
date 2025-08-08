class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            print(stack)
            if ch in pairs:  # 它是反向的
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()  # stack 要么不是空，且stack[-1] == pairs[ch]
            else:
                stack.append(ch)

        return not stack

    def isValid_1(self, s: str) -> bool:
        """
        栈先入后出特点恰好与本题括号排序特点一致，即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，则遍历完所有括号后 stack 仍然为空；
        :param s:
        :return:
        """
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        print(stack)
        return len(stack) == 1

if __name__ == "__main__":
    a = "{([])}()("
    resp = Solution().isValid_1(a)
    print(resp)
