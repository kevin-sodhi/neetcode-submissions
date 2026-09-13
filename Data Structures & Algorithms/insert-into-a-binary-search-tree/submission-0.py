# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if root is None:
            return node
        
        curr = root

        while curr:
            ## In BST smaller value goes to left and bigger value goes to right
            if val > curr.val:
                if curr.right is None:
                    curr.right = node
                    break
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    break
                curr = curr.left
        
        return root




                
        