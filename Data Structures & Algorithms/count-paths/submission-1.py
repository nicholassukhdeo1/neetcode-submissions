class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recTraverse(curr_row,curr_col,row_bound,col_bound,cache):

            if curr_row == row_bound or curr_col == col_bound:
                return 0
            if cache[curr_row][curr_col] > 0:
                return cache[curr_row][curr_col]
            if curr_row == row_bound-1 and curr_col == col_bound-1:
                return 1

            cache[curr_row][curr_col] = (recTraverse(curr_row+1,curr_col,row_bound,col_bound,cache) + recTraverse(curr_row,curr_col+1,row_bound,col_bound,cache))

            return cache[curr_row][curr_col]

        cache = [[0] * n for i in range(m)]

        return recTraverse(0,0,m,n,cache)