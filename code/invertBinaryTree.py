# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        history = []
        if root == None:
            return root
        history.append(root)
        while history:
            current_root = history.pop(0)
            current_root.left, current_root.right = (
                current_root.right,
                current_root.left,
            )
            if current_root.left:
                history.append(current_root.left)
            if current_root.right:
                history.append(current_root.right)
        return root
