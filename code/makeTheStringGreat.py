class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        res = ""

        stack.append(s[0])
        i = 1

        while i < n:
            if stack and stack[-1] != s[i] and stack[-1].upper() == s[i].upper():
                stack.pop()
            else:
                stack.append(s[i])
            i += 1

        while stack:
            res += stack.pop()

        return res[::-1]
