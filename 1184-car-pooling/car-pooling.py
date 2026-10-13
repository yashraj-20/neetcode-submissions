class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # i = 0
        # j = i + 1
        # n = len(trips)
        trips.sort(key = lambda x: x[1])

        # max_cap = trips[i][0]

        # while i < n-1 and j < n:
        #     if trips[i][2] > trips[j][1]:
        #         max_cap += trips[j][0]
        #         j += 1
        #         if max_cap > capacity:
        #             return False
        #     else:
        #         max_cap -= trips[i][0]
        #         i += 1
        
        # return True
        heap = []
        max_people = 0
        for count, start, end in trips:
            while heap and start >= heap[0][0]:
                drop, people = heapq.heappop(heap)
                max_people -= people
            
            max_people += count

            if max_people > capacity:
                return False
            
            heapq.heappush(heap, (end, count))
        
        return True