class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by the starting value of each interval
        intervals.sort(key=lambda x: x[0])
        # The merged list to return
        merged = []
        # Iterate through each interval
        for interval in intervals:
            # If merged is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # If there is overlap, merge the intervals
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
