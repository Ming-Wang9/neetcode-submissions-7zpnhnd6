class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols= len(matrix), len(matrix[0])
        zero = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] ==0:
                    zero.append([r,c])
        #zero row 
        for z in zero:
            for c in range(cols):
                matrix[z[0]][c] = 0
        #zero col 
        for z in zero:
            for r in range(rows):
                matrix[r][z[1]] = 0
        

