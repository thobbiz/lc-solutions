from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize the result list and the queue with the root
        result = []
        queue = deque([root])

        # Process the tree level by level
        while queue:
            # Determine the number of nodes at the current level
            level_size = len(queue)
            current_level = []

            # Iterate exactly 'level_size' times to process this level only
            for _ in range(level_size):
                # Pop the oldest node (First-In, First-Out)
                node = queue.popleft()

                # Add the value to the current level's list
                current_level.append(node.val)

                # Add children to the queue for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the finished level to the final result
            result.append(current_level)

        return result
