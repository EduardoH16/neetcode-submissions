# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue, heap = deque([root]), []
        while queue:
            node = queue.popleft()
            if node:
                heapq.heappush(heap, node.val)
                queue.append(node.left)
                queue.append(node.right)
        for i in range(1, k+1):
            val = heapq.heappop(heap)
            if i == k:
                return val
        
