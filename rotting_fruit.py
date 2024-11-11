class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #update states every minute 
        #use bfs with q
        #queue holds all rotting oranges
        #first use row * col loop to add rotting to q, and count fresh in grid
        #then write a bfs that ends when no more fresh or no more queue

        queue = collections.deque()
        fresh = 0
        mins = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1: 
                    fresh += 1 
        
        while queue and fresh > 0: 
            for temp in range(len(queue)): 
                row, col = queue.popleft()

                for change_row, change_col in directions: 
                    new_row = change_row + row
                    new_col = change_col + col
                    if new_row < 0 or new_row >= rows or\
                        new_col < 0 or new_col >= cols or\
                        grid[new_row][new_col] == 0: 
                        continue

                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        fresh -= 1
                        

            mins += 1

        if fresh == 0: return mins
        else: return -1
