class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #brute force

        max_area = 0

        arr_len = len(heights)

        for i in range(arr_len):
            for j in range(i+1, arr_len):
                if heights[i] > heights[j]:
                    curr_area = heights[j]*(j-i)
                else:
                    curr_area = heights[i]*(j-i)
                if curr_area > max_area:
                    max_area = curr_area


        return max_area