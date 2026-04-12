class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r,t,b = 0,len(matrix[0])-1, 0, len(matrix)-1
        row = 0
        while t<=b:
            mrow = t+(b-t)//2
            if matrix[mrow][l] <= target <= matrix[mrow][r]:
                row= mrow
                break
            if target < matrix[mrow][l]:
                b=mrow-1
            if target>matrix[mrow][r]:
                t=mrow+1
        if not (t<=b):
            return False
        while l<=r:
            m=l+(r-l)//2
            if target == matrix[row][m]:
                return True
            if target > matrix[row][m]:
                l=m+1
            if target < matrix[row][m]:
                r=m-1
        return False