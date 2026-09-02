class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
                res += 1
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    res -= 1
                else:
                    res += 1

        return res
