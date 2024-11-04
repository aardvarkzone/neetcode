from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Approach: BFS
        
        # Variables:
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(row, col): 
            queue = deque([(row, col)])  
            visited = [[False] * num_cols for _ in range(num_rows)]
            visited[row][col] = True
            steps = 0
            
            while queue: 
                for _ in range(len(queue)):
                    check_row, check_col = queue.popleft()
                    if grid[check_row][check_col] == 0: 
                        return steps
                    for change_row, change_col in directions: 
                        new_row, new_col = check_row + change_row, check_col + change_col  # Use check_row, check_col
                        if (0 <= new_row < num_rows and 
                            0 <= new_col < num_cols and
                            not visited[new_row][new_col] and
                            grid[new_row][new_col] != -1):
                            visited[new_row][new_col] = True
                            queue.append((new_row, new_col))
                steps += 1
            return INF
                    
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == INF: 
                    grid[row][col] = bfs(row, col)
