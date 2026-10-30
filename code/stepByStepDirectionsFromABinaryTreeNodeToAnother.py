# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        parent = {root: None}
        start = None
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == startValue:
                start = node
            for child in (node.left, node.right):
                if child:
                    parent[child] = node
                    stack.append(child)

        queue = deque([start])
        visited = {start}
        prev = {start: (None, "")}
        node = start

        while queue:
            node = queue.popleft()
            if node.val == destValue:
                break
            for nxt, step in ((node.left, "L"), (node.right, "R"), (parent[node], "U")):
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    prev[nxt] = (node, step)
                    queue.append(nxt)

        path = []
        while node is not start:
            node, step = prev[node]
            path.append(step)

        return "".join(reversed(path))
