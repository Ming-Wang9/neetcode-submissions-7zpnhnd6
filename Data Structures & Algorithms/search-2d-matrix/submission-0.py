class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l, r = 0, len(matrix[row])-1
            while l <=r:
                m = l +(r-l)//2
                if matrix[row][m] > target:
                    r -= 1
                elif matrix[row][m] < target:
                    l += 1
                else:
                    return True
        return False