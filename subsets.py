class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        #use range 2^n for total num of subsets
        for index in range(1 << n): 
            output.append([nums[j] for j in range(n) if (index & (1 << j))])

        return output
