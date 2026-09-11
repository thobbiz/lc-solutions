from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        stack = []
        res = []

        while curr:
            res.append(0)
            curr = curr.next

        idx = 0
        curr = head
        while curr:
            while stack and curr.val > stack[-1][0]:
                res[stack.pop()[1]] = curr.val
            stack.append((curr.val, idx))
            idx += 1
            curr = curr.next

        return res
