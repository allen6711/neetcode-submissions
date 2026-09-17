class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        visited = set()
        left = 0
        n = len(s)
        for right in range(n):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])

            max_count = max(max_count, right - left + 1)
        
        return max_count