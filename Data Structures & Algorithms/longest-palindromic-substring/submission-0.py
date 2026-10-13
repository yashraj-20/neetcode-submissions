class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start, max_len = 0, 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1>max_len:
                        start = i
                        max_len = j-i+1
        
        return s[start:start+max_len]