from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


maxDiameter = 0


def diameterRecur(root):
    global maxDiameter
    if root is None:
        return 0

    lHeight = diameterRecur(root.left)
    rHeight = diameterRecur(root.right)

    maxDiameter = max(maxDiameter, lHeight + rHeight)

    return 1 + max(lHeight, rHeight)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maxDiameter
        maxDiameter = 0

        diameterRecur(root)

        return maxDiameter
