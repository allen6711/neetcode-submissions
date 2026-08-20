class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 1
        dp = [[False] * n for _ in range(n)]
        start = 0

        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and length > max_length:
                    max_length = length
                    start = i
        
        return s[start:start + max_length]