from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        new = []
        for i, c in enumerate(customers):
            if grumpy[i] == 0:
                satisfied += c
                new.append(0)
            else:
                new.append(c)

        max_technique = 0
        for c in range(minutes):
            max_technique += new[c]

        l = 0
        curr = max_technique
        for r in range(minutes, len(new)):
            curr = curr - new[l] + new[r]
            max_technique = max(max_technique, curr)
            l += 1

        return max_technique + satisfied
