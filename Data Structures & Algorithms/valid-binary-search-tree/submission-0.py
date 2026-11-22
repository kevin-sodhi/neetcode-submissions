# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def ValidateTree(node,min_val,max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            
            left = ValidateTree(node.left,min_val,node.val)
            right = ValidateTree(node.right,node.val,max_val)
            return left and right
        
        return ValidateTree(root,float('-inf'),float('+inf'))
        '''
        we need to check the left subtree and right subtree 
            - if we have a max_val and min_val 
            - each curr node will compare to the max value and min value of the tree to validate

        '''