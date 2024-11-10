class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer 
        #check areas as you go inwards, return max area 
        left = 0 
        right = len(heights) - 1
        curr = 0
        while left < right: 
            temp = min(heights[left], heights[right]) * (right - left)
            
            curr = max(temp, curr)
            if heights[left] <= heights[right]: left += 1
            else: right -= 1
        return curr
