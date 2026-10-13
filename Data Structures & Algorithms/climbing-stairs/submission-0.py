class Solution:
    def climbStairs(self, n: int) -> int:
        # [1,2,3,5]
        dp = [0] * (n)
        if n < 3:
            return n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]