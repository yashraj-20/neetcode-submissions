class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def df(i, buying):
            if i > len(prices)-1:
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            if buying:
                buy = -prices[i] + df(i+1, False)
                no_buy = df(i+1, True)

                res = max(buy, no_buy)
            else:
                sell = prices[i] + df(i+2, True)
                hold = df(i+1, False)

                res = max(sell, hold)
            dp[(i, buying)] = res
            return res
        return df(0, True)