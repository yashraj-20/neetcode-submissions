class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        heap = [[-freq, val] for val, freq in dic.items()]
        heapq.heapify(heap)
        count = 0

        while heap:
            temp = []
            for i in range(n+1):
                
                if not heap:
                    if temp:
                        count += 1
                    continue
                freq, proc = heapq.heappop(heap)
                
                count += 1
                if freq + 1 < 0:
                    temp.append([freq+1, proc])
                
            heap.extend(temp)     # keep whatever was left un-popped
            heapq.heapify(heap)

        return count