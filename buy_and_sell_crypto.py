class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        output = 0

        while right < len(prices): 
            if prices[left] < prices[right]: 
                profit = prices[right] - prices[left]
                output = max(output, profit)
            else: 
                left = right
        
            right += 1

        return output
