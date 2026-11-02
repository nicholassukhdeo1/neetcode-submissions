class Solution:
    def solve(self, board: List[List[str]]) -> None:


        row_len = len(board)
        col_len = len(board[0])

        my_queue = deque()

        # up,down,left,right
        


        def DFS(r,c):

            if r < 0 or r == row_len:
                return
            if c < 0 or c == col_len:
                return
            if board[r][c] == "X" or board[r][c] == "T":
                return

            
            board[r][c] = "T"

            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)

            return

        for r in range(row_len):
            for c in range(col_len):
                if board[0][c] == "O": 
                    DFS(0,c)
                if board[r][0] == "O":
                    DFS(r,0)
                if board[(row_len-1)][c] == "O":
                    DFS((row_len-1),c)
                if board[r][(col_len-1)] == "O":
                    DFS(r,(col_len-1))

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
