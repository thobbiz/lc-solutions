class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        res = 1
        head = points[0][1]

        for p in points[1:]:
            if p[0] > head:
                res += 1
                head = p[1]
            else:
                head = min(head, p[1])

        return res
