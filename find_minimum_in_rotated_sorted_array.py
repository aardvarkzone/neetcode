class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right: 
            #if arr already sorted
            if nums[left] < nums[right]: 
                output = min(output, nums[left])
                break

            middle = left + (right-left)//2

            output = min(output, nums[middle])

            #if left half is sorted, move left pointer up to right side
            if nums[middle] >= nums[left]: 
                left = middle + 1
            #else move right pointer down to left side
            else:
                right = middle - 1
        
        return output
