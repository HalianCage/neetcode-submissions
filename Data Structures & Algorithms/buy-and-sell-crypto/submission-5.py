class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Profit, l, r = 0, 0, 1

        while r < len(prices):

            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                Profit = max(Profit, diff)
            else:
                l = r

            r += 1
            

            
        return Profit

        