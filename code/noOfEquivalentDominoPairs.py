from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashMap = {}
        res = 0

        for i in dominoes:
            key = tuple(sorted(i))
            hashMap[key] = hashMap.get(key, 0) + 1

        for val in hashMap.values():
            res += val * (val - 1) // 2

        return res
