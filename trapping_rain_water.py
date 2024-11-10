class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointer
        #keep track of both indices (left and right pointers)
        #keep track of right and left max sides
        #if leftMax < rightMax, move left pointer, check new leftMax
        #leftMax - height[left] is added water
        #if rightMax < leftMax, move right pointer, check new rightMax
        #rightMax - height[right] is added water
        if not height: return 0

        left_pointer = 0
        right_pointer = len(height) - 1

        left_max = height[left_pointer]
        right_max = height[right_pointer]

        total = 0

        while left_pointer < right_pointer: 
            if left_max < right_max:
                left_pointer += 1
                left_max = max(height[left_pointer], left_max)
                total += left_max - height[left_pointer]
            else:
                right_pointer -= 1
                right_max = max(height[right_pointer], right_max)
                total += right_max - height[right_pointer]
        
        return total


