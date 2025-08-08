
def coinChange(coins, amount):
    """
    :type coins: List[int]  # 可用的硬币面额
    :type amount: int       # 需要凑成的总金额
    :rtype: int             # 最少需要的硬币数，如果无法凑成则返回-1
    """
    # 初始化dp数组，dp[i]表示凑成金额i所需的最少硬币数
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 金额为0时不需要任何硬币

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp)

    return dp[amount] if dp[amount] != float('inf') else -1


def coinChange_1(coins, amount):
    memo = {}  # 记忆化字典

    def helper(remain):
        if remain < 0:
            return -1
        if remain == 0:
            return 0
        if remain in memo:
            return memo[remain]

        min_coins = float('inf')
        for coin in coins:
            res = helper(remain - coin)
            if res >= 0 and res < min_coins:
                min_coins = res + 1

        memo[remain] = min_coins if min_coins != float('inf') else -1
        print(memo)
        return memo[remain]

    return helper(amount)


def coinChangeWays(coins, amount):
    """
    如果需要计算所有可能的兑换方式（而不只是最少硬币数），可以使用以下方法：
    这个变种问题中，dp[i]表示凑成金额i的所有可能方式的数量。
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # 金额为0时有1种方式（不选任何硬币）

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    # coins = [2]
    amount = 11
    resp = coinChange(coins, amount)
    # resp = coinChange_1(coins, amount)
    # resp = coinChangeWays(coins, amount)
    print(resp)