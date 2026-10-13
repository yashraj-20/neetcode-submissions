class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(index, current):
            if index == len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            backtracking(index+1, current)
            current.pop()
            backtracking(index+1, current)

        backtracking(0, [])
        return result
             

