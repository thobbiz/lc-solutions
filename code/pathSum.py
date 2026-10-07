# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        curr = root
        currCount = 0

        def dfs(curr, currCount):
            if not curr:
                return False

            currCount += curr.val
            left = curr.left
            right = curr.right

            if currCount == targetSum:
                if not(left or right):
                    return True

            return dfs(left, currCount) or dfs(right, currCount)

        return dfs(curr, 0)
