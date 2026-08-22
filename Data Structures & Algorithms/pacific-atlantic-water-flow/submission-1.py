class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        # more time efficient to find elements in a set vs. an array
        atl = set()
        pac = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(row,col,visit,prev_node):
            # base cases
            if row > rows-1 or col > cols-1 or row < 0 or col < 0 or (row,col) in visit or prev_node > heights[row][col]:
                return
            visit.add((row,col))

            dfs(row+1,col,visit,heights[row][col])
            dfs(row-1,col,visit,heights[row][col])
            dfs(row,col+1,visit,heights[row][col])
            dfs(row,col-1,visit,heights[row][col])

        
        # populate pacific's set

        for col in range(cols):
            dfs(0,col,pac,heights[0][col])

        for row in range(rows):
            dfs(row,0,pac,heights[row][0])

        # populate atlantic's set

        for col in range(cols):
            dfs(rows-1,col,atl,heights[rows-1][col])

        for row in range(rows):
            dfs(row,cols-1,atl,heights[row][cols-1])

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row,col])

        return res