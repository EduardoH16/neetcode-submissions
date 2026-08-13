# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, queue = [], deque()
        queue.append(root)
        while queue:
            qLen = len(queue)
            last_val = -101
            for _ in range(qLen):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    last_val = node.val
            if last_val != -101:
                res.append(last_val)
        return res
            
                    