from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.right = deque()
        self.left = deque()
    def pushFront(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.appendleft(val)


    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        if len(self.right) > len(self.left):
            self.left.append(self.right.popleft())

    def popFront(self) -> int:
        if not self.left:
            return -1
        val = self.left.popleft()
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

        return val

    def popMiddle(self) -> int:
        if not self.left:
            return -1
        val = self.left.pop()
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

        return val

    def popBack(self) -> int:
        val = -1
        if self.right:
            if len(self.left) > len(self.right):
                self.right.appendleft(self.left.pop())
            val = self.right.pop()
        elif self.left:
            return self.left.pop()

        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
