class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer sliding window 
        #variable window 
        #first --> check if left < right
        #if not, set left equal to right, increment right by 1 
        #if left < right, then check for max output, incr right by 1
        left = 0 
        right = 1
        output = 0 

        while right < len(prices): 
            if prices[left] < prices[right]: 
                output = max(prices[right] - prices[left], output)
            else: 
                left = right
            right += 1
        return output
