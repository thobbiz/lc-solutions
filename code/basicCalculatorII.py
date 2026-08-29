class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        last_sign = "+"
        curr_no = 0
        for i, c in enumerate(s):
            if c.isdigit():
                curr_no = (curr_no * 10) + int(c)

            if c in "+*-/" or i == len(s) - 1:
                if last_sign == "+":
                    stack.append(int(curr_no))
                elif last_sign == "-":
                    stack.append(-int(curr_no))
                elif last_sign == "*":
                    res = stack.pop() * curr_no
                    stack.append(res)
                elif last_sign == "/":
                    res = int(stack.pop() / curr_no)
                    stack.append(res)

                last_sign = c
                curr_no = 0
        return sum(stack)
