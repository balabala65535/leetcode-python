
def combinationSum(candidates, target):
    ans = []
    comb = []

    def dfs(target, idx):
        if idx == len(candidates):
            return
        if target == 0:
            ans.append(comb.copy())
            return
        # 直接跳过当前数字
        dfs(target, idx + 1)
        # 选择当前数字
        if target - candidates[idx] >= 0:
            comb.append(candidates[idx])
            dfs(target - candidates[idx], idx)
            comb.pop()

    dfs(target, 0)
    return ans