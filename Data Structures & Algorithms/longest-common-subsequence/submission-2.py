class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp1 = [0] * len(text1)
        # dp2 = [0] * len(text2)

        # for i in range(len(text1)):
        #     for j in range(len(text2)):
        #         if text1[i] == text2[j]:
        #             dp1[i] = 1
        #             dp2[j] = 1
        # return min(sum(dp1), sum(dp2))
        # n1 = len(text1)
        # n2 = len(text2)
        # dp = [[None] * (n1+1) for _ in range(n2+1)]
        dp = {}
        def df(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                return 1 + df(i+1, j+1)
            dp[(i,j)] = max(df(i,j+1),df(i+1,j))
            return dp[(i,j)]
        
        return df(0,0)
                

        
        