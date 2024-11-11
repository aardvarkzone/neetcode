class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #change all surrounded O regions to X 
        #need all four sides (corners are safe)
        #use dfs, modify board directly no need for sets
        #cases for "O" 
        #1) edge - ignore
        #2) lone "O" surrounded by X 4 sides
        #3) group of O surrounded by X 4 sides
        #4) group of O not completely surrounded

        if not board or not board[0]: 
            return

        rows = len(board)
        cols = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(row, col): 
            if not (0 <= row < rows and 0 <= col < cols and board[row][col] == 'O'):
                return 
            board[row][col] = "S"
            for change_row, change_col in directions:
                dfs(change_row + row, change_col + col)

        for row in range(rows):
            if board[row][0] == "O": dfs(row, 0)
            if board[row][cols - 1] == "O": dfs(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == "O": dfs(0, col)
            if board[rows - 1][col] == "O": dfs(rows - 1, col)

        for row in range(rows): 
            for col in range(cols): 
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
