# Definition for singly-linked list.
from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)

        priorityQ = [head for head in lists if head]
        heapify(priorityQ)

        dummy = current = ListNode()

        while priorityQ:
            node = heappop(priorityQ)
            if node.next:
                heappush(priorityQ, node.next)
            current.next = node
            current = current.next

        return dummy.next
