class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def df(i):
            jump = 1e9
            if i == len(nums)-1:
                return 0
            if i in dp:
                return dp[i]

            for x in range(1, nums[i]+1):
                if i+x < len(nums):
                    jump = min(jump, 1+df(i+x))
            dp[i] = jump
            return jump

        return df(0)