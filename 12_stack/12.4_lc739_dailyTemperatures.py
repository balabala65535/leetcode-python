from typing import List


class Solution:
    def dailyTemperatures(self, temperatures):
        length = len(temperatures)
        max_temp = temperatures[0]
        max_temp_index = 0
        day_dict = {'0': 0}
        for i in range(1, length):
            day_dict[str(i)] = 0
            if temperatures[i] < max_temp:
                day_dict[str(max_temp_index)] += 1
            else:
                max_temp = temperatures[0]
                max_temp_index = i

            if temperatures[i] > temperatures[i - 1]:
                day_dict[str(i-1)] += 1

        return [day_dict[str(i)] for i in range(length)]

    def dailyTemperatures_1(self, temperatures):
        """暴力"""
        n = len(temperatures)
        ans, nxt, big = [0] * n, dict(), 10 ** 9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(temperatures[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[temperatures[i]] = i
        return ans

    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        """单调栈"""
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
