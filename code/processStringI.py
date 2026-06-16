class Solution:
    def processStr(self, s: str) -> str:
        def reverse(s: str):
            return s[::-1]

        def duplicate(s: str):
            return s + s

        def removeLast(s: str):
            return s[:-1]

        result = ""

        for c in s:
            if c == "*":
                result = removeLast(result)
            elif c == "#":
                result = duplicate(result)
            elif c == "%":
                result = reverse(result)
            else:
                result = result + c

        return result
