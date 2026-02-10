class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def add(self, node):
        afterHead = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = afterHead
        afterHead.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.delete(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(self.map[key])

        newNode = Node(key, value)
        self.map[key] = newNode
        self.add(newNode)

        if len(self.map) > self.capacity:
            lruNode = self.tail.prev
            self.delete(lruNode)
            del self.map[lruNode.key]


def main():

    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(capacity)
    param_1 = obj.get(key)
    obj.put(key, value)

    s1 = "a"
    s2 = "eidbaooo"

    # Run the code
    result = checkInclusion(s1, s2)
    print(result)

    s1 = "ab"
    s2 = "eidboaoo"

    # Run the code
    result = checkInclusion(s1, s2)
    print(result)

    s1 = "a"
    s2 = "ab"

    result = checkInclusion(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
