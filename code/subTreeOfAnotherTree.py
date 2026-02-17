from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
    if node1 and node2:
        if node1.val == node2.val:
            left = isSameTree(node1.left, node2.left)
            right = isSameTree(node1.right, node2.right)
            return left and right
        return False
    return node1 == node2


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
