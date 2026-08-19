class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visited = [[False for col in range(cols)] for row in range(rows)]

        res_index = 0

        def helper(row,col,res_index):

            # always consider the order of your base cases..

            # if letter is out of bounds:
            if row > rows-1 or col > cols-1 or row < 0 or col < 0:
                return False

            # if letter != the letter in the word:
            if board[row][col] != word[res_index]:
                return False

            if visited[row][col] == True:
                return False

            if res_index == (len(word)-1):
                return True


            # do
            
            if board[row][col] == word[res_index]:
                res_index += 1

            visited[row][col] = True

            # recurse

            if (helper(row+1,col,res_index) or
            helper(row-1,col,res_index) or
            helper(row,col+1,res_index) or
            helper(row,col-1,res_index)):
                return True

            # undo
            visited[row][col] = False
            res_index -= 1

            return False
        
        for row in range(rows):
            for col in range(cols):
                if helper(row,col,res_index):
                    return True
          
        return False