class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)-1
        while t <= b:
            m = t +(b-t) //2
            if matrix[m][0] > target:
                b = m-1
            elif matrix[m][-1] < target:
                t = m+1
            else:
                break
        if not (t <= b):
            return False
            
        l, r = 0, len(matrix[0])-1
        row = t + (b -t) //2
        while l <=r:
            row_m =l +(r-l) //2
            if matrix[row][row_m] > target:
                r =row_m - 1
            elif matrix[row][row_m] < target:
                l =row_m + 1
            else:
                return True
        return False
