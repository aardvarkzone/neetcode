class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        output = right

        while left <= right: 
            k = left + (right - left) // 2
            time = 0
            for pile in piles: 
                time += math.ceil(float(pile) / k)
            if time <= h: 
                output = k
                right = k - 1
            else: 
                left = k + 1
                
        return output
