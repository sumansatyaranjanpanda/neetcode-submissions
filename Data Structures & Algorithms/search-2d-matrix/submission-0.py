class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        rows=len(matrix)
        cols=len(matrix[0])


        l=0
        r=(rows*cols)-1


        while l<=r:
            mid=l+(r-l)//2

            row= mid//cols
            col= mid%cols

            if matrix[row][col]==target:
                return True
            elif target> matrix[row][col]:
                l=mid+1
            else:
                r=mid-1

        return False





        
