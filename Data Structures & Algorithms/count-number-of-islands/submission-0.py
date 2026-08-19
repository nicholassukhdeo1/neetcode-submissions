class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        rows = len(grid)
        cols = len(grid[0])

        island_count = 0
        

        isVisited = [[False for col in range(cols)] for row in range(rows)]

        def helper(row,col):

            # base cases

            # if youre off the grid, return false
            if row > rows-1 or col > cols-1 or row < 0 or col < 0:
                return

            if isVisited[row][col]:
                return
                
            if grid[row][col] == "0":
                return

            # do (guards false positives.)
            
            isVisited[row][col] = True

            # recurse (now, for )
            # if (left,right,up,down)
            helper(row+1,col)
            helper(row-1,col)
            helper(row,col+1)
            helper(row,col-1)

            # undo??
            

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and isVisited[row][col] == False:
                    island_count += 1
                    helper(row,col)
                    

        return island_count