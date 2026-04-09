import math
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        inMST = [False] * N
        minDistance = [math.inf] * N
        res = 0

        minDistance[0] = 0

        for _ in range(N):
            cur = -1
            for i in range(N):
                if not inMST[i] and (cur == -1 or minDistance[i] < minDistance[cur]):
                    cur = i

            inMST[cur] = True
            res += minDistance[cur]

            x1, y1 = points[cur]
            for j in range(N):
                if not inMST[j]:
                    x2, y2 = points[j]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    if d < minDistance[j]:
                        minDistance[j] = d

        return res
