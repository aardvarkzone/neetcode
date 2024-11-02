class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_rows = len(grid)
        num_cols = len(grid[0])
        counter = 0
        def dfs(row, col): 
            if (row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] == "0"):
                return 

            grid[row][col] = "0"

            for shift_row, shift_col in directions: 
                dfs(shift_row + row, shift_col + col)
        
        for row in range(num_rows): 
            for col in range(num_cols): 
                if grid[row][col] == "1":
                    dfs(row, col)
                    counter += 1

        return counter


