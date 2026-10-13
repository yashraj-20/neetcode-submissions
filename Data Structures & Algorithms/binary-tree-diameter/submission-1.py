# Definileft_tion for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_len = self.depth(root.left)
        right_len = self.depth(root.right)
        dai = left_len + right_len
        len_sub_dai = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(dai, len_sub_dai)

    def depth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.depth(root.left), self.depth(root.right))