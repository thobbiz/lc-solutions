class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i == len(s):
                break
            if t[j] == s[i]:
                i += 1
        return i == len(s)
