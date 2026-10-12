# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(currNode, currSum):
            if not currNode:
                return 0

            currSum = (currSum * 10) + currNode.val

            if not currNode.left and not currNode.right:
                return currSum

            return dfs(currNode.right, currSum) + dfs(currNode.left, currSum)

        return dfs(root, 0)
