class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        row_len = len(matrix)
        col_len = len(matrix[0])
        size = row_len * col_len

        res = []

        s_x = left
        s_y = top

        while len(res) < size:

            # top

            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            # right
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            # bottom
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])

            bottom -= 1
            # left
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left += 1


        return res