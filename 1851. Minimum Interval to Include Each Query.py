from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((q, i) for i, q in enumerate(queries))
        res = [-1] * len(queries)
        pq = []
        i = 0
        for q, idx in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            res[idx] = pq[0][0] if pq else -1
        return res