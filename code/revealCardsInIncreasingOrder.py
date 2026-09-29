from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0] * n
        q = deque(range(n))

        for card in deck:
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())

        return res
