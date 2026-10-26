class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        max_area = []
        row_len = len(grid)
        col_len = len(grid[0])
        res = 0
        visited = set()


        def dfs(row,col):

            # base case
            if (row,col) in visited:
                return 0
            if row > (row_len - 1) or row < 0:
                return 0
            if col > (col_len - 1) or col < 0:
                return 0
            if grid[row][col] == 0:
                return 0

            visited.add((row,col))

            # do

            
            area = (1 +
            dfs(row+1,col) +
            dfs(row-1,col) +
            dfs(row,col+1) +
            dfs(row,col-1))

            # print(f"area is: {area}")

            # undo

            return area

        # find a valid starting point. that is, 

        for row in range(row_len):
            for col in range(col_len):
                # print(f"starting index is r: {row}, c:{col}")
                curr_area = dfs(row,col)
                # print(f"curr_area is {curr_area}")

                res = max(res,curr_area)
                # print(f"res is {res}")

        return res


            