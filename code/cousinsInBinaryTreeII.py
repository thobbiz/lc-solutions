# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        root.val = 0
        queue = deque([root])

        while queue:
            next_level_sum = 0
            for node in queue:
                if node.left:
                    next_level_sum += node.left.val
                if node.right:
                    next_level_sum += node.right.val

            for _ in range(len(queue)):
                node = queue.popleft()
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val

                if node.left:
                    node.left.val = next_level_sum - sibling_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = next_level_sum - sibling_sum
                    queue.append(node.right)

        return root
