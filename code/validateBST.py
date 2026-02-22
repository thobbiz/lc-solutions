from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBST(self, root: Optional[TreeNode], low: int, high: int) -> bool:
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return self.isBST(root.left, low, root.val) and self.isBST(
            root.right, root.val, high
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = float("inf")
        low = float("-inf")
        return self.isBST(root, low, high)
