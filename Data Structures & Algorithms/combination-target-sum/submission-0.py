class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(i, curr):
            if sum(curr) == target:
                result.append(curr.copy())
                return
            
            if i == len(nums) or sum(curr) > target:
                return

            curr.append(nums[i])
            backtracking(i, curr)
            curr.pop()
            backtracking(i+1, curr)
        
        backtracking(0, [])
        return result