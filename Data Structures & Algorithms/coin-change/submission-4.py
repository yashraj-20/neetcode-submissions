class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [0] * len(coins)
        # result = 0
        # for i in range(len(dp)-1, -1, -1):
        #     if amount == 0:
        #         return result
            
        #     if coins[i] > amount:
        #         continue

        #     result += amount//coins[i]
        #     amount = amount%coins[i]
        # return result if amount == 0 else -1
        dp = {}
        def dfs(t):
            if t == 0:
                return 0
            if t in dp:
                return dp[t]
            res = 1e9
            for coin in coins:
                if t-coin >= 0:
                    res = min(res, 1 + dfs(t-coin))
            dp[t] = res
            return res
        res = dfs(amount)
        return -1 if res == 1e9 else res
                
