from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        hashMap = {}
        current = head
        copyHead = Node(0)
        trail = copyHead

        # copy all nodes(apart from the random)
        while current:
            node = Node(current.val)
            trail.next = node
            trail = trail.next
            hashMap[current] = node
            current = current.next

        # copy random pointer
        current = head
        while current:
            hashMap[current].random = (
                hashMap[current.random] if current.random else None
            )
            current = current.next

        return copyHead.next
