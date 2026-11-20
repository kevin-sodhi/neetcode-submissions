# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            ## find on the left of the Tree
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            ## find on the right of the tree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    
        
        
        '''
        This is a Bin Search Tree means :
            a value less than the node goes = left
            a value greater than the node goes = right
        so, if p is less than the Node search left
            if p is greater than the Node search left 
            what should we do ? 

        '''