# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left_skip, left_rob = dfs(node.left)
            right_skip, right_rob = dfs(node.right)

            skip = max(left_skip, left_rob) + max(right_skip, right_rob)
            rob = node.val + left_skip + right_skip

            return (skip, rob)

        return max(dfs(root))
