class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        need = len(count_t)
        formed = 0

        window = defaultdict(int)
        left = 0
        n = len(s)
        min_left = 0
        min_len = float('inf')

        for right in range(n):
            char = s[right]
            window[s[right]] += 1

            if char in count_t and count_t[char] == window[char]:
                formed += 1

            while formed == need:
                if right - left + 1 < min_len:
                    min_left = left
                    min_len = right - left + 1
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t and window[left_char] < count_t[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]

        


                