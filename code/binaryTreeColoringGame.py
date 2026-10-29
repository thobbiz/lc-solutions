# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode | None, n: int, x: int) -> bool:
        left_size = 0
        right_size = 0

        def count(node):
            nonlocal left_size, right_size
            if not node:
                return 0

            left = count(node.left)
            right = count(node.right)

            if node.val == x:
                left_size = left
                right_size = right

            return left + right + 1

        count(root)
        parent_size = n - left_size - right_size - 1

        return max(left_size, right_size, parent_size) > n // 2
