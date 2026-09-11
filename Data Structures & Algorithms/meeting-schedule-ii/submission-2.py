"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # build your start and end arrays

        size = len(intervals)

        if size == 1:
            return 1

        elif size == 0:
            return 0

        # lets call each interval i. then we access the start of each i.

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s_index = 0;
        e_index = 0;


        res = 0
        count = 0

        while s_index < size:
            if start[s_index] < end[e_index]:
                count += 1
                s_index += 1
            else:
                count -= 1
                e_index += 1

            res = max(res,count)

        return res
