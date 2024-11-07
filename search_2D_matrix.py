from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left = 0
        right = num_rows * num_cols - 1  

        while left <= right: 
            middle = left + (right - left) // 2
            
            row = middle // num_cols  
            col = middle % num_cols   
            
            if target > matrix[row][col]: 
                left = middle + 1    
            elif target < matrix[row][col]: 
                right = middle - 1    
            else: 
                return True           
        
        return False
