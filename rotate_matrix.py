class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for x in range(len(matrix)): 
            for y in range(x + 1, len(matrix)):
                temp = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp
