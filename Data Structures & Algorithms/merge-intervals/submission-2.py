class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        size = len(intervals)
        res = []

        if size == 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])


        prev_interval = intervals[0]

        for index in range(1,size):
            if prev_interval[1] < intervals[index][0]:
                res.append(prev_interval)
                prev_interval = intervals[index]
            # if intervals[index][0] > prev_interval[1]:
            #     res.append(intervals[index])
            else: 
                prev_interval[0] = min(prev_interval[0],intervals[index][0])
                prev_interval[1] = max(prev_interval[1], intervals[index][1])

            

        if prev_interval not in res:
            return res + [prev_interval]
        return res

            