class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])

        row = len(matrix)

        top = 0
        bottom = row-1

        left = 0
        right = col-1

        while top<=bottom:
            mid_row = (top+bottom)//2

            if target == matrix[mid_row][0]:
                return True
            
            if target<matrix[mid_row][0]:
                bottom = mid_row - 1
            
            elif target>matrix[mid_row][0]:
                top = mid_row + 1

        if bottom < 0:
            return False

        mid_row = bottom
        
        while left<=right:
            mid_col = (left+right)//2

            if target == matrix[mid_row][mid_col]:
                return True
            
            if target <= matrix[mid_row][mid_col]:
                right = mid_col-1
            elif target >= matrix[mid_row][mid_col]:
                left = mid_col + 1

        print(mid_col)
        
        return False
            

        
                
            





        