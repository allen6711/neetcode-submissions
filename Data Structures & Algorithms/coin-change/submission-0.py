class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for cur_amount in range(1, amount + 1):
            for coin in coins:
                if cur_amount >= coin:
                    dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - coin] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]