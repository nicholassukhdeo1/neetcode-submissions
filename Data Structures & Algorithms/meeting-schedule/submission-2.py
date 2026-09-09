"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # if u find one overlapping interval, brutal


        size = len(intervals)

        if size == 1 or size == 0:
            return True

        intervals.sort(key=lambda intervals: intervals.start)

        prev_interval = intervals[0]

        for index in range(1,size):
            if prev_interval.end <= intervals[index].start:
                prev_interval = intervals[index]
            else:
                return False



        return True
