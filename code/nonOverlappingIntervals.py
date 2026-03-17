import math
from typing import List


class Solution:
    def eraseOverlapIntervalsDP(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0
        end = -math.inf

        for start, curr_end in intervals:
            if start >= end:
                end = curr_end
            else:
                count += 1

        return count
