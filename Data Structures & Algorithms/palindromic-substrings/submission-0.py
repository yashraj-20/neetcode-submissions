class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        result = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            result+=1
            for j in range(i+1, n):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    result+=1
        
        return result