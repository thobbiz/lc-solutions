from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = {0: 1}
        result = 0

        def findSum(node, prefixSum):
            nonlocal result
            if node == None:
                return
            prefixSum += node.val
            result += count.get((prefixSum - targetSum), 0)
            count[prefixSum] = count.get(prefixSum, 0) + 1

            findSum(node.left, prefixSum)
            findSum(node.right, prefixSum)

            count[prefixSum] -= 1

        findSum(root, 0)
        return result
