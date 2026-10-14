# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        queue = deque([target])
        seen = {target}
        dist = 0

        while queue:
            if dist == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            dist += 1

        return []
