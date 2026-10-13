class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current =[]

        def backtracking(index):
            result.append(current.copy())
            
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtracking(i+1)
                current.pop()
        backtracking(0)
        return result

                
        #     current.append(nums[index])
        #     backtracking(index+1, current)
        #     current.pop()
        #     backtracking(index+1, current)

        # backtracking(0, [])
        # return result
             

