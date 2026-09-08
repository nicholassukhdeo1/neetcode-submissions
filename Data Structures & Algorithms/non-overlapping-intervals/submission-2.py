class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        size = len(intervals)
        count = 0
        if size == 1:
            return 0



        intervals.sort(key=lambda intervals: intervals[0])

        prev_interval = intervals[0]


        for index in range(1,size):
            if prev_interval[1] <= intervals[index][0]:
                prev_interval = intervals[index]
            else:
                count += 1
                if prev_interval[1] < intervals[index][1]:
                    prev_interval = prev_interval
                else:
                    prev_interval = intervals[index]
                # prev_interval[0] = min(prev_interval[0],intervals[index][0])
                # prev_interval[1] = max(prev_interval[1],intervals[index][1])





        return count
