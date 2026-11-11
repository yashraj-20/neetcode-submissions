# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dp = {}
        def df(root):
            if not root:
                return None
            
            if root == p or root == q:
                return root

            left = df(root.left)
            right = df(root.right)
            
            if left and right:
                return root
            
            if left:
                return left

            return right

        return df(root)