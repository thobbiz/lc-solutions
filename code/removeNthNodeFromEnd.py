from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy
        front = dummy

        for _ in range(n):
            front = front.next

        while front.next:
            front = front.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
