class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #iterate with rows
        #now need to check posDiag, negDiag, col
        #use sets
        #posDiag = r + c 
        #negDiag = r - c
        #use backtracking recursion 

        col, posDiag, negDiag = set(), set(), set()
        output = []

        board = []
        for i in range(n):
            board.append(['.'] * n)

        def backtrack(r): 
            if r == n:
                temp = [''.join(row) for row in board]
                output.append(temp)
                return
            
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue 
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
            
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return output
