class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]
        def df(i, prev):
            if i == len(nums):
                return 0
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]
            leng = 0 + df(i+1, prev)
            if nums[i] > nums[prev] or prev == -1:
                take = 1 + df(i+1, i)
                leng = max(take, leng)
            dp[i][prev+1] = leng
            return leng
        return df(0,-1)
            


