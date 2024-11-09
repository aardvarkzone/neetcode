class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if empty, return 0
        #sort nums
        #if nums[i] == nums[i-1] + 1, add to streak
        #if nums[i] == nums[i-1], keep streak same and continue
        #else add streak to list, reset streak 
        #return max of list 
        if not nums: return 0 
        nums.sort()

        counter_list = []
        streak = 1

        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1] + 1: 
                streak += 1
            elif nums[i] == nums[i - 1]: 
                continue 
            else: 
                counter_list.append(streak)
                streak = 1
        #handles case of longest string being last one
        counter_list.append(streak)
        
        return max(counter_list)
