# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Preorder: Root -> Left -> Right
        Inorder:  Left -> Root -> Right
        Postorder : Left -> Right -> Root

        # to get the index of the root node we can get it from preorder[0]
        the method is using inorder list for root and preorder list for making child
        preorder = [1,2,3,4] and inorder = [2,1,3,4]
        the preorder[0] will gives us the root 
            then the we get index of preorder[0] in inorder list
            then the left side of idx(preorder[0]) in inorder is left subtree 
            and the right side is right subtree 

        '''
        if not preorder or not inorder:
            return None
        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i
        
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)


