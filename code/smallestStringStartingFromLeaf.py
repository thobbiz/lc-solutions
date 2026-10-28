# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        num_to_alpha = {i: char for i, char in enumerate(string.ascii_lowercase)}

        def dfs(node, currString):
            if not node:
                return None

            currString = num_to_alpha[node.val] + currString
            left = node.left
            right = node.right

            if not left and not right:
                return currString

            leftRes = dfs(left, currString)
            rightRes = dfs(right, currString)

            if leftRes is None:
                return rightRes
            if rightRes is None:
                return leftRes

            return min(leftRes, rightRes)

        return dfs(root, "")
