class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = -1
        R = len(heights) - 1
        L = 0
        for count in range(len(heights)):

            curr_area = min(heights[L], heights[R]) * (R-L)

            if curr_area > max_area:
                max_area = curr_area
            
            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            elif heights[L] == heights[R]:
                L += 1
                R -= 1
            
            
            
        return max_area

        # the further you go out, the better the width is
        # because the bottleneck wont change

        #width is best at init. 

        #shift the smaller bar.

        