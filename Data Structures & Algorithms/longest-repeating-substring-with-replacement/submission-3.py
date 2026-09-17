class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_count = 0
        n = len(s)
        left = 0
        ans = 0
        for right in range(n):
            counts[s[right]] += 1
            max_count = max(max_count, counts[s[right]])
            
            while (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans