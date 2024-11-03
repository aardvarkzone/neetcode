class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()

        #dfs increments area counter for every new piece of land connected
        def dfs(row, col): 
            #check if not within bounds, water, or visited, return 0
            if ((row, col) in visited or row < 0 or row == num_rows or col < 0 or col == num_cols or grid[row][col] == 0):
                return 0
            
            visited.add((row, col))

            return (1 + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1))
        
        area = 0
        for row in range(num_rows): 
            for col in range(num_cols): 
                area = max(area, dfs(row, col))

        return area
      
