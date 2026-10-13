class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []

        def backtracking(open, close):
            if len(curr) == 2*n:
                result.append("".join(curr))
                return

            if open<n:
                curr.append("(")
                backtracking(open+1, close)
                curr.pop()

            if close<open:
                curr.append(")")
                backtracking(open, close+1)
                curr.pop()

        backtracking(0,0)
        return result










        #     # print(curr)
        #     if curr.count("(") == curr.count(")"):
        #         joint = "".join(curr)
        #         if joint not in result:
        #             result.append(joint)

        #     for i in range(start, len(nums)):
        #         curr.append(nums[i])
        #         # if len(curr)%2 != 0:
        #         #     continue
                
        #         backtracking(i+1)
        #         curr.pop()
        
        # backtracking(0)
        # print(result)
        # return result