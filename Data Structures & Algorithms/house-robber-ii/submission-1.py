class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp_array(arr):
            n = len(arr)
            dp = [0] * (n + 1)
            dp[1] = arr[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + arr[i - 1], dp[i - 1])
            return dp[n]

        return max(dp_array(nums[1:]), dp_array(nums[:-1]))