class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals = [[1,2],[3,5],[9,10]], newInterval = [4,8]
        # [[1,2],[3,8],[9,10]]
        res = []
        i = 0
        n = len(intervals)

        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res