from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                top = stack[-1]
                stack.append(top * 2)
            elif op == "C":
                _ = stack.pop()
            else:
                stack.append(int(op))
        res = 0
        while stack:
            res += stack.pop()
        return res
