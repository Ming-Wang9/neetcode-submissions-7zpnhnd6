class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        t,b,l,r = 0, rows-1, 0, cols-1
        targetrow = float('inf')
        while t<=b:
            mr = t+(b-t)//2
            if matrix[mr][0] <= target <= matrix[mr][-1]:
                targetrow = mr 
                break
            elif matrix[mr][0] > target:
                b = mr-1
            elif matrix[mr][-1] < target:
                t=mr+1
        if targetrow == float('inf'):
            return False
        while l<=r:
            m = l+(r-l)//2
            if matrix[targetrow][m] == target:
                return True
            elif matrix[targetrow][m] > target:
                r=m-1
            else:
                l=m+1
        return False