class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        L = 0 * n
        R = (m * n) - 1

        # still m * n
        mid = (L+R) // 2

        while L <= R:
            adj_row = mid // n
            adj_col = mid % n

            if target == matrix[adj_row][adj_col]:
                return True

            # dont consider mid because it wasnt the target anyways
            if target > matrix[adj_row][adj_col]:
                L = mid+1
            if target < matrix[adj_row][adj_col]:
                R = mid-1

            mid = (L+R) // 2

        return False