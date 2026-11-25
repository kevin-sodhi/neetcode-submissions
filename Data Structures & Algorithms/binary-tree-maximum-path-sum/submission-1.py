# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def DFS(node):
            nonlocal max_sum 
            if not node:
                return 0
            left = max(0,DFS(node.left))
            #print("left: ", left)
            right = max(0,DFS(node.right))
            #print("right: ", right)
            #. max path sum without split
            currentSum = node.val + left + right
            #print("currentSum", currentSum)
            max_sum = max(max_sum,currentSum)
            return node.val + max(left,right)
        DFS(root)
        return max_sum
        
        
        
        '''
        we need to find the path that have max sum
            - path can be a single node 
            - path can be number of nodes as long as the edges are connected to each next node
            Q. where do start traversing ?
            Q. how do we make a valid path 
            # we need to keep track of the sum 
            # at the end we need to have a max sum 
            Pesudo algo:
                max_sum = -inf
                DFS(node):
                    Base case:
                        if node is None:
                            return 0
                    Calculate maximum contribution from left subtree
                    Calculate maximum contribution from right subtree
                    Ignore negative contributions
                    Calculate path passing through current node:
                    currentSum = node.val + left + right
                    Update global maxSum
                    Return node.val + max(left, right)
                    Call DFS(root)  
                    Return maxSum
        '''
        