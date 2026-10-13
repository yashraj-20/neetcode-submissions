class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        candidates.sort()

        def backtrack(start):
            total = sum(curr)
            if total == target:
                result.append(curr.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if total + candidates[i] > target:
                    break

                curr.append(candidates[i])
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        return result