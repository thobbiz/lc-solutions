class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapST = {}
        hashMapTS = {}
        for c1, c2 in zip(s, t):
            if (c1 in hashMapST and hashMapST[c1] != c2) or (
                c2 in hashMapTS and hashMapTS[c2] != c1
            ):
                return False
            hashMapST[c1] = c2
            hashMapTS[c2] = c1

        return True
