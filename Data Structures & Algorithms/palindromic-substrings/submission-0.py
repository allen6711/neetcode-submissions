class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [False] * n
        count = 0
        for j in range(n):
            for i in range(j + 1):
                dp[i] = (s[i] == s[j] and (j - i <= 1 or dp[i + 1]))
                
                if dp[i]:
                    count += 1
        
        return count