class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def df(i,j):
            if j == len(word2):
                return len(word1)-i
            if i == len(word1):
                return len(word2)-j
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] == word2[j]:
                return df(i+1, j+1)
            else:
                res = (1 + min(df(i, j+1),df(i+1, j),df(i+1, j+1)))
            dp[(i,j)] = res
            return res
        return (df(0,0)) 