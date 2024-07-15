
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        prevend = intervals[0][1]
        remove = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]>=prevend:
                prevend= intervals[i][1]
            else:
                remove +=1
        return remove
