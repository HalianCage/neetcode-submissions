class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Profit, l, r = 0, 0, 0

        while l < len(prices) and r < len(prices):

            if l == r:
                r += 1
                continue

            diff = prices[r] - prices[l]

            if diff < 0:
                l = r
                r += 1
            else:
                Profit = max(Profit, diff)
                r += 1

            
        return Profit

        