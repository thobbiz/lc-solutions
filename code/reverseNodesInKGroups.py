from tokenize import group
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kthNode = getKth(groupPrev, k)
            if not kthNode:
                break

            nextGroupHead = kthNode.next

            prev, curr = nextGroupHead, groupPrev.next
            while curr != nextGroupHead:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            newGroupTail = groupPrev.next
            groupPrev.next = kthNode

            groupPrev = newGroupTail

        return dummy.next
