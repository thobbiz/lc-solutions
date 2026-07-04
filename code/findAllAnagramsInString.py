from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        pCount = {}
        sCount = {}
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
        result = [0] if sCount == pCount else []
        for i in range(len(p), len(s)):
            left = s[i - len(p)]
            right = s[i]
            sCount[right] = sCount.get(right, 0) + 1
            sCount[left] -= 1
            if sCount[left] == 0:
                del sCount[left]
            if sCount == pCount:
                result.append(i - len(p) + 1)
        return result
