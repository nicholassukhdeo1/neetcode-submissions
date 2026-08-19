class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # each helper call explores an entire island
        rows = len(grid)
        cols = len(grid[0])

        isVisited = [[False for col in range(cols)] for row in range(rows)]

        island_count = 0

    
        def helper(row,col):

            # base cases (when to stop exploring)

            # if the neighbor that we look @ out of range?
            if row > rows-1 or col > cols-1 or row < 0 or col < 0:
                return
            # if neighbor is a 0
            if grid[row][col] == "0":
                return
            # if neighbor has been already explored
            if isVisited[row][col] == True:
                return

            isVisited[row][col] = True

            # recursive calls (explore all neighbors inside island)
            helper(row+1,col)
            helper(row-1,col)
            helper(row,col+1)
            helper(row,col-1)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and isVisited[row][col] == False:
                    helper(row,col)
                    island_count += 1

        return island_count

