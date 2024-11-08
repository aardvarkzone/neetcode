class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #cases:
        #1) multiple 0s - return 0 
        #2) 1 zero - everything but arr[index of 0] is 0, arr[index of 0] = product
        #3) 0 zero - arr[index] = product // num
        
        product = 1 
        zero_count = 0 
        arr = [0] * len(nums)

        for num in nums:
            if num: product *= num
            else: zero_count += 1
        
        if zero_count > 1: return arr

        for index, num in enumerate(nums): 
            if zero_count == 1:
                if not num: 
                    arr[index] = product
            else: 
                arr[index] = product // num
        return arr
