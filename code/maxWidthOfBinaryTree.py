# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        res = 0
        q = deque([(root, 0)])

        while q:
            size = len(q)
            first = q[0][1]
            last = q[-1][1]
            res = max(res, last - first + 1)

            for _ in range(size):
                node, idx = q.popleft()
                idx -= first

                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))

        return res
