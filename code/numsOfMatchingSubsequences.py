from typing import List
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            it = iter(w)
            waiting[next(it)].append(it)

        res = 0

        for c in s:
            advance = waiting.pop(c, [])
            for it in advance:
                nxt = next(it, None)
                if nxt is None:
                    res += 1
                else:
                    waiting[nxt].append(it)

        return res
