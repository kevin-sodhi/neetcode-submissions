# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Empty list edge Case
        if not head or not head.next:
            return
        
        # 1. find the mid-point 
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # 2. slpit the list into 2 parts
        p1 = head
        p2 = slow.next
        slow.next = None
        # 3. reverse the second list
        curr = p2
        prev = None
        while curr is not None:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        # 4. merge the list 
        p1 = head
        p2 = prev
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2










        





