class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            elif c == ")":
                top = stack[-1]
                if top == 0:
                    stack.append(1)
                else:
                    stack.append(top * 2)

            return stack[-1]
