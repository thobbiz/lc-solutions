class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time

        # q = deque()

        # for t in tickets:
        #     q.append(t)

        # pos = k
        # while q and tickets[pos] > 0:
        #     curr = t.popleft() - 1
        #     if curr > 0:
        #         q.append(curr)
        #     if pos == 0:
        #         print()
