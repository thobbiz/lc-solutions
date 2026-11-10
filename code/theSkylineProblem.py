class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort()

        res = []
        heap = [(0, float('inf'))]

        for x, neg_h, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_h:
                heapq.heappush(heap, (neg_h, right))
            max_h = -heap[0][0]
            if not res or res[-1][1] != max_h:
                res.append([x, max_h])

        return res
