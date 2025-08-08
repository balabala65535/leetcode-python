from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0  # int(1e9) 表示一个大整数
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
