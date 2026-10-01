class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # probably bit manip bc of o(1) space
        
        # brute force

        row_count = len(matrix)
        col_count = len(matrix[0])

        rowZero = False


        for r in range(row_count):
            for c in range(col_count):
                if(matrix[r][c] == 0):
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    elif r == 0:
                        rowZero = True
                    
                

        for r in range(1,row_count):
            for c in range(1,col_count):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(row_count):
                matrix[r][0] = 0

        if rowZero:
            for c in range(col_count):
                matrix[0][c] = 0
            


    

        

        