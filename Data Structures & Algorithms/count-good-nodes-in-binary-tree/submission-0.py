# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS
        from collections import deque
        if root is None:
            return 0
        
        max_so_far = float('-inf')
        queue = deque([(root, max_so_far)])
        count = 0

        while queue:
            for _ in range(len(queue)):
                node, max_so_far = queue.popleft()
                if node.val >= max_so_far:
                    count += 1
                
                max_so_far = max(max_so_far, node.val)

                if node.left:
                    queue.append((node.left, max_so_far))
                
                if node.right:
                    queue.append((node.right, max_so_far))
        
        return count