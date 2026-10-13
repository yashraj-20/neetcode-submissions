class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []

        intervals.sort(key=lambda x: x[0])

        while i < n:
            if res and res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            
            i += 1
        
        return res
