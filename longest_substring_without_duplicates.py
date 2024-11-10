class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window with set -- variable window
        #make left and right at start
        #set holds chars within the window
        #incr right to expand, left to shrink 
        #every time left shifts, calc the length of window and update max 

        left = 0
        window = set()
        output = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            output = max(output, right - left + 1)
        return output
        
