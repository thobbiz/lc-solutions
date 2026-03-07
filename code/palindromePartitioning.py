from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtrack(i):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if isPalin(i, j):
                    part.append(s[i:j + 1])
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)
        return res
