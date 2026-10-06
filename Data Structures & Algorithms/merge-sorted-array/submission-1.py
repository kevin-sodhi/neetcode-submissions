class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [10,20,20,40,0,0]     m = 4
        # nums2 = [1,2]                 n = 2

        p1 = m-1  # p1 at the last valid element of nums1
        p2 = n-1  # p2 at the last ele of nums2
        p = m+n -1 # last ele of nums1

        while p2 >= 0:  # going untill p2 = 0
        # checking p1>=0 and last vaild ele of num1 > last valid ele of nums2
            if p1>=0 and nums1[p1] > nums2[p2]: 
                # if greater swap last ele of nums1 with greater ele
                nums1[p] = nums1[p1]
                # changes teh pointer to one step back
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

            

                
            




        