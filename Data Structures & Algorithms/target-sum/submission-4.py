class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i,total) in dp:
                return dp[(i,total)]

            add = backtrack(i + 1, total + nums[i])
            subtract = backtrack(i + 1, total - nums[i])
            res = add + subtract
            dp[(i, total)] = res
            return res

        return backtrack(0, 0)
