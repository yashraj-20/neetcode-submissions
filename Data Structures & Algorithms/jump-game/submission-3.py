class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def df(i):
            if i == len(nums)-1:
                return True
            if i in dp:
                return dp[i]
            for x in range(1, nums[i]+1):
                if df(i+x):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return df(0)