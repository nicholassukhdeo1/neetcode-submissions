class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source BFS

        row_len = len(grid)
        col_len = len(grid[0])

        #up, down, right, left
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        my_queue = deque()
        visited = [[False for col in range(col_len)] for row in range(row_len)]

        # start at each goal in the map
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 0:
                    my_queue.append((r,c))
                    visited[r][c] = True
                    # print(f"I start multi-source at row {r} and {c}")

        steps = 0


        while my_queue:
            for _ in range(len(my_queue)):
                row, col = my_queue.popleft()
                for dr,dc in directions:
                    nr, nc = dr+row, dc+col

                    # if it is land, redefine it right now

                    # its land if.. its NOT 0, NOT -1, AND in bounds.

                    if((nr >= 0 and nr < row_len) and (nc >= 0 and nc < col_len)
                    and (grid[nr][nc] != 0) and (grid[nr][nc] != -1)
                    and (visited[nr][nc] == False)):
                        grid[nr][nc] = min(steps+1,grid[nr][nc])
                        visited[nr][nc] = True
                        my_queue.append((nr,nc))

            steps += 1