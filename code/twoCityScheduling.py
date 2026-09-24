class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        n = len(costs) // 2
        bCost = 0
        res = 0
        bToA = []

        for i in costs:
            bCost += i[1]
            bToA.append(i[0] - i[1])

        bToA.sort()
        for s in bToA[:n]:
            res += s
        res += bCost

        return res
