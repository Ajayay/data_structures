class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_stock = 1000000
        max_stock = 0
        profit = 0
        profit_sum = 0
        for i in range(n):
            if prices[i]<min_stock:
                min_stock = prices[i]
            else:
                profit += prices[i]-min_stock
                min_stock = prices[i]
            
        return profit
            