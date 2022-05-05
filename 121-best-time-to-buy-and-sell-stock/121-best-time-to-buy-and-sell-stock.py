class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 100000
        max_val = 0
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                if  prices[i]-min_val > max_val:
                    max_val = prices[i]-min_val

        return max_val 
        