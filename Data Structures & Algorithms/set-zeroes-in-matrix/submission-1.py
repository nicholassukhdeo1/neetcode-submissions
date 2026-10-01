class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # probably bit manip bc of o(1) space
        
        # brute force

        row_count = len(matrix)
        col_count = len(matrix[0])

        row_target = []
        col_target = []


        for r in range(row_count):
            for c in range(col_count):
                if(matrix[r][c] == 0):
                    row_target.append(r)
                    col_target.append(c)
                    
                

        for r,c in zip(row_target,col_target):
            for cdx in range(col_count):
                matrix[r][cdx] = 0
            for rdx in range(row_count):
                matrix[rdx][c] = 0
            


    

        

        