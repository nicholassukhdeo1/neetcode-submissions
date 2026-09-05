class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        # we know by default that all intervals smaller than new interval's start 
        # are valid, independent intervals
        res = []

        for index in range(len(intervals)):
            if intervals[index][1] < newInterval[0]:
                res.append(intervals[index])
            elif intervals[index][0] > newInterval[1]:
                return res + [newInterval] + intervals[index:]
            else:
                newInterval[0] = min(newInterval[0],intervals[index][0])
                newInterval[1] = max(newInterval[1],intervals[index][1])

        

        return res + [newInterval]
