class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def df(i, target):
            res = 0
            if i == len(coins):
                return 0
            if target == 0:
                return 1
            if (i, target) in dp:
                return dp[(i, target)]
            res += df(i+1, target)
            if coins[i] <= target:
                res += df(i, target-coins[i])
            dp[(i, target)] = res
            return res
        return df(0, amount)