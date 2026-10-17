from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None)])

        while queue:
            found_x = found_y = False
            parent_x = parent_y = None

            for _ in range(len(queue)):
                node, parent = queue.popleft()

                if node.val == x:
                    found_x = True
                    parent_x = parent
                if node.val == y:
                    found_y = True
                    parent_y = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if found_x and found_y:
                return parent_x != parent_y
            if found_x or found_y:
                return False

        return False
