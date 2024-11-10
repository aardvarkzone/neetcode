class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointer 
        #sort the array for two pointer, skip dups
        #both pointers try to reach 0 with curr num 
        #skip dups
        #adjust pointer based on sum < or > 0
        #if == 0, then move pointers to avoid dups and check for subsequent dups

        output = []
        nums.sort()

        for index in range(len(nums) - 2): 
            if index > 0 and nums[index] == nums[index - 1]: continue 
        
            left = index + 1
            right = len(nums) - 1

            while left < right: 
                temp = nums[index] + nums[left] + nums[right]
                if temp == 0: 
                    output.append([nums[index], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1

                elif temp < 0: 
                    left += 1
                else: 
                    right -= 1
            
        return output



