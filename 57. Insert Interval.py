class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1

        start, end = newInterval[0],newInterval[1]
        while i  < len(intervals) and intervals[i][0]<=newInterval[1]:            
            start = min(intervals[i][0],start)
            end = max(intervals[i][1],end)
            i += 1
        res.append([start,end])
        while i  < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
