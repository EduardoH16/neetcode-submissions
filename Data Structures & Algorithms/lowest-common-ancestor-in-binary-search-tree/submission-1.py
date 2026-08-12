# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root: 
            if p.val < root.val and q.val > root.val:
                return root
            elif p.val > root.val and q.val < root.val:
                return root
            else:
                if root.left == p and root.right == q:
                    return root
                elif root.left == q and root.right == p:
                    return root
                elif root == p or root == q:
                    return root
                else:
                    return (self.lowestCommonAncestor(root.left, p, q)
                        or self.lowestCommonAncestor(root.right, p, q))

