class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
        return res