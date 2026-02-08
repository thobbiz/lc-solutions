class TimeMap:
    def __init__(self):
        self.histories = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.histories:
            self.histories[key] = []
        self.histories[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.histories:
            return ""
        left, right, pos = 0, len(self.histories[key]) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if self.histories[key][mid][0] <= timestamp:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1
        if pos == -1:
            return ""
        return self.histories[key][pos][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
