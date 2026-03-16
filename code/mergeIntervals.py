from typing import List


class Solution:
    def mergeBruteForce(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort()
        result = []

        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]

            if result and result[-1][1] >= end:
                continue

            for j in range(i + 1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
            result.append([start, end])

        return result

    def mergeOptimal(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort()

        result = []
        result.append(intervals[0])

        for i in range(1, n):
            last = result[-1]
            curr = intervals[i]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                result.append(curr)

        return result
