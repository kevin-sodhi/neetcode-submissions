# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## Middle of List is slow
        curr = slow
        prev = None
        ## we need to reverse the list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #
        pOne = head
        pTwo = prev
        while pOne and pTwo:
            if pOne.val != pTwo.val:
                return False
            pOne = pOne.next
            pTwo = pTwo.next
        return True




