def generateParenthesis(n: int):
    my_str = '()' * n
    result_str = []
    result = []
    left_str = my_str.split()

    def backtrack(result_str, left_str, start_index):
        if len(left_str) == 0:
            result.append(''.join(result_str.copy()))
            return
        result_str.append(left_str[start_index])
        left_str.pop(start_index)
        backtrack(result_str, left_str, start_index + 1)
        result_str.pop()

    backtrack(result_str, left_str, 0)
    return result


def generateParenthesis_1(n: int):
    my_str = '()' * n
    result_str = []
    result = []
    left_str = my_str.split()

    def backtrack(left, right):
        nonlocal result_str
        if left == right == n:
            left = right = 0
            result.append(''.join(result_str.copy()))
            result_str = []
            return
        if left <= right:
            result_str.append('(')
            left += 1
            backtrack(left, right)
        if left > right:
            result_str.append(')')
            right += 1
            backtrack(left, right)

    backtrack(0, 0)
    return result


class Solution:
    def generateParenthesis(self, n: int):
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
                else:
                    print("啥也不是，滚", A)
            else:
                print(A)
                A.append('(')
                generate(A)
                A.pop()
                print("==到我拉", A)
                A.append(')')
                generate(A)
                print("==it's me:", A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans

    def generateParenthesis_1(self, n: int):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                # print('=====')
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                print('left < n:', S)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                print('right < left:', S)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == "__main__":
    n = 3
    resp = Solution().generateParenthesis_1(3)
    print(resp)
