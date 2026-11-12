# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for i in range(len(lists)):
            res = self.mergeTwoLists(res, lists[i])
        return res
        
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next 
            curr = curr.next
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2
        return dummy.next

        '''
        we can take the first 2 linked list (sorted)
            and merge them and then again use the algo to murge the new and the next sorted
        
        how do we merge lists[0] and lists[1]?
            we can iterate through both the list 
            and compare the each element and 
                if the element is == or <then then we will link it to the next node
        '''
        


        
        

        