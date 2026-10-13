# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif not subRoot:
            return True
        
        if self.checker(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def checker(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root or subRoot:
            if root and subRoot and root.val == subRoot.val:
                return self.checker(root.right, subRoot.right) and self.checker(root.left, subRoot.left)
            else:
                return False

        