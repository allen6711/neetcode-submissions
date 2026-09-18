class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        n = len(nums)
        ans = []
        dq = deque()
        
        for right in range(n):
            while dq and dq[0] <= right - k:
                dq.popleft()
            
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            if right - k + 1 >= 0:
                ans.append(nums[dq[0]])
            
        return ans