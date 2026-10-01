from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        dq = deque()
        total = 0
        left = 0
        best = 0

        for right in range(len(chargeTimes)):
            total += runningCosts[right]

            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)

            while left <= right and chargeTimes[dq[0]] + (right - left + 1) * total > budget:
                total -= runningCosts[left]
                if dq[0] == left:
                    dq.popleft()
                left += 1

            best = max(best, right - left + 1)

        return best
