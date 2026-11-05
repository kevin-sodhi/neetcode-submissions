# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1. we can take a dummy Node
        '''
        #1. 
        dummy = ListNode(0,head)
        left = dummy
        right = head

        # shifting right till the nth value
        while n > 0 and right:
            right = right.next
            n-=1
        
        # left and right pointer shifting till right reaches Null
        while right:
            left = left.next
            right = right.next
        
        # remove the Node
        left.next = left.next.next
        return dummy.next







        




        