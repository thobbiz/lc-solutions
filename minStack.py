class MinStack:
    def __init__(self):
        self.mainstack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.mainstack.append(val)

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.mainstack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.mainstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
