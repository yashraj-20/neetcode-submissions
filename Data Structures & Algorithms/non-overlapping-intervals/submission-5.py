class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        n = len(intervals)
        res = []
        count = 0

        intervals.sort(key=lambda x: x[1])

        while i < n:
            if res and res[-1][1] > intervals[i][0]:
                count += 1
            else:
                res.append(intervals[i])
            
            i += 1
        
        return count
