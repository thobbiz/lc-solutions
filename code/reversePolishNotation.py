from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/":
                right_element = stack.pop()
                left_element = stack.pop()

                match c:
                    case "+":
                        result = right_element + left_element
                        stack.append(result)
                    case "-":
                        result = left_element - right_element
                        stack.append(result)
                    case "*":
                        result = right_element * left_element
                        stack.append(result)
                    case _:
                        result = int(left_element / right_element)
                        stack.append(result)
            else:
                stack.append(int(c))
        return stack[0]
