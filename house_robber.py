class Solution:
    def rob(self, nums: List[int]) -> int:
        #DP
        #cannot rob adj houses 
        #find the max money that can be robbed for every ith house
        #build up to n 
        #max_money[i] = either previous house, or i-2 total + current
        
        if not nums: return 0

        n = len(nums)

        if n == 1: return nums[0]

        max_money = [0] * n 
        max_money[0] = nums[0]
        max_money[1] = max(max_money[0], nums[1])
        
        for i in range (2, n):
            max_money[i] = max(max_money[i-1], nums[i] + max_money[i-2])

        return max_money[n-1]
