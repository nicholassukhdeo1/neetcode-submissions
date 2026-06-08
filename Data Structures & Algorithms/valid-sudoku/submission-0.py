class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # what if you use a set.. and as you're iterating thru
        # the entire graph, you do a check every 9 iteration

        graph_count = defaultdict(int)

        # row check
        for i in range(9):
            graph_count = defaultdict(int)
            for j in range(9):
                if board[i][j] != '.':
                    graph_count[board[i][j]] += 1
                    if graph_count[board[i][j]] > 1:
                        return False

        # column check
        for col in range(9):
            graph_count = defaultdict(int)
            for row in range(9):
                if board[row][col] != '.':
                    graph_count[board[row][col]] += 1
                    if graph_count[board[row][col]] > 1:
                        return False

        # 3x3 box check
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                graph_count = defaultdict(int)
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            graph_count[board[i][j]] += 1
                            if graph_count[board[i][j]] > 1:
                                return False

        return True



