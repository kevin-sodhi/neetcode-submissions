# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1. we can reverse the list 
        2. we can iterate through the list for n steps
        3. remove the node 
        4. take the list reverse it again
        '''
        def ReverseList(head):
            prev = None
            curr = head
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        # 1. we can reverse the list 
        curr = ReverseList(head)
        # 2. we can iterate through the list for n steps
        temp = curr
        prev = None
        for i in range(1,n):
            prev = temp
            temp = temp.next
        #3. 3. remove the node 
        if prev is None:
            curr = temp.next
        else:
            prev.next = temp.next
        # 4. reverse the list again
        return ReverseList(curr)






        




        