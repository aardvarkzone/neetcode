class Solution:
    def rob(self, nums: List[int]) -> int:
        #DP
        #use the same logic as linear problem, but 
        #this time check for everything but last house vs everything but first house
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))

    def dp(self, nums: List[int]) -> int: 
        if not nums: return 0 
        n = len(nums)
        if n == 1: return nums[0]
        
        max_money = [0] * n
        
        max_money[0], max_money[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n): 
            max_money[i] = max(max_money[i - 1], max_money[i - 2] + nums[i])
        
        return max_money[n - 1]
        
