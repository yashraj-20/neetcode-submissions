class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2 != 0:
            return False
        target = target//2
        dp = [[None] * (target+1) for _ in range(len(nums))]
        def df(i, target):
            if i == len(nums):
                return False
            if target == 0:
                return True
            if dp[i][target] is not None:
                return dp[i][target]
            not_take = df(i+1, target)
            take = False
            if nums[i] <= target:
                take = df(i+1, target-nums[i])
            dp[i][target] = take or not_take
            return take or not_take
        return df(0, target)
