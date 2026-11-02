class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        row_len = len(grid)
        col_len = len(grid[0])
        time = 0
        f_fruit = 0

        # up,down,left,right
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = [[False for col in range(col_len)] for row in range(row_len)]

        my_queue = deque()



        for r in range(row_len):
            for c in range(col_len):

                # if its rotting, add it
                if grid[r][c] == 2:
                    my_queue.append((r,c))
                    visited[r][c] = True
                if grid[r][c] == 1:
                    f_fruit += 1

        if f_fruit == 0:
            return 0


        while my_queue:
            

            for _ in range(len(my_queue)):
                row, col = my_queue.popleft()

                for dr,dc in directions:
                    nr,nc = row+dr,col+dc

                    if ((nr >= 0 and nr < row_len) and (nc >= 0 and nc < col_len)
                    and (grid[nr][nc] == 1) and (visited[nr][nc] == False)):
                        grid[nr][nc] = 2
                        f_fruit -= 1
                        visited[nr][nc] = True
                        my_queue.append((nr,nc))

            time += 1
            if f_fruit == 0:
                break

        if f_fruit == 0:
            return time
        else:
            return -1



