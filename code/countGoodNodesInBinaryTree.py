# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, root, maxVal) -> int:
        if not root:
            return 0

        if root.val >= maxVal:
            self.result += 1
            maxVal = root.val

        self.DFS(root.left, maxVal)
        self.DFS(root.right, maxVal)

    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.DFS(root, root.val)
        return self.result
