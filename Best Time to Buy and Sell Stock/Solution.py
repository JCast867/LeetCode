from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0    # left is buying
        right = 1   # right is selling
        maxProfit = 0

        while right < len(prices):
            # profitable transaction?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left += right
            right = 1

        return maxProfit
