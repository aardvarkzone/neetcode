class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #make set for row, col, and sub-box
        #make LIST of sets to track all 9 
        #populate sets with spaces for 1-9 
        #skip empty '.'
        #need to keep track of which box -     
        
        row_set_list = [set() for temp in range(9)]
        col_set_list = [set() for temp in range(9)]
        box_set_list = [set() for temp in range(9)]

        for row in range(9): 
            for col in range(9): 
                val = board[row][col]
                if val == '.': continue 

                which_box = (row // 3) * 3 + (col // 3)

                if (val in row_set_list[row]) or \
                   (val in col_set_list[col]) or \
                   (val in box_set_list[which_box]): 
                    return False

                row_set_list[row].add(val)
                col_set_list[col].add(val)
                box_set_list[which_box].add(val)

        return True
