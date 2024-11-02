class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        
        counter = []
        current_streak = 1  
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1: current_streak += 1   
            elif nums[i] == nums[i - 1]: continue
            else:
                counter.append(current_streak)
                current_streak = 1
        
        counter.append(current_streak)
        
        return max(counter)
