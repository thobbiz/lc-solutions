from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alp = "abcdefghijklmnopqrstuvwxyz"
        alp_map = {}
        for index, letter in enumerate(alp, start=0):
            alp_map[letter] = index

        rev_alp = alp[::-1]

        res = ""

        for word in words:
            weight = 0
            for letter in word:
                ind = alp_map[letter]
                weight += weights[ind]
            rev_ind = weight % 26
            res += rev_alp[rev_ind]

        return res
