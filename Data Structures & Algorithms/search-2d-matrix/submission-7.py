class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0, len(matrix)-1
        l,r= 0, len(matrix[0])-1
        target_row = float('inf')
        while top<=bottom:
            mid_row = top+(bottom-top)//2
            if matrix[mid_row][0]<=target<=matrix[mid_row][-1]:
                target_row=mid_row
                break
            elif matrix[mid_row][-1]<target:
                top=mid_row+1
            elif matrix[mid_row][0]>target:
                bottom=mid_row-1
        if target_row == float('inf'):
            return False
        while l<=r:
            m=l+(r-l)//2
            if matrix[target_row][m]==target:
                return True
            elif matrix[target_row][m]<target:
                l=m+1
            else:
                r=m-1
        return False

