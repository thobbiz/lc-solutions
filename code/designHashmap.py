class MyHashSet:
    def __init__(self):
        self.buckets = []
        for i in range(50):
            self.buckets.append([])

    def add(self, key: int) -> None:
        i = self.getIndex(key)
        if not self.contains(key):
            self.buckets[i].append(key)

    def remove(self, key: int) -> None:
        i = self.getIndex(key)
        if self.contains(key):
            self.buckets[i].remove(key)

    def contains(self, key: int) -> bool:
        i = self.getIndex(key)
        return key in self.buckets[i]

    def getIndex(self, key: int):
        return key % len(self.buckets)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
