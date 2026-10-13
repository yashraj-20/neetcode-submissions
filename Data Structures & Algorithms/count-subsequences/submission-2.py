class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def df(i,j):
            res = 0
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:
                res = df(i+1, j+1) + df(i+1, j)
            else:
                res += df(i+1, j)

            dp[(i,j)] = res
            return res
        
        return df(0,0)
                