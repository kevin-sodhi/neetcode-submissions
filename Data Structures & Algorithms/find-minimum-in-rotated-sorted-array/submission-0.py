class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[right]
        
        '''
        Brute force solution will be go through the Array one by one and find the min

        we have nums that is rotated n times
            if nums is rotated 1 time 
        '''
    
    def binsearch(nums,target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            if nums[mid]> target:
                right = mid-1
        return -1

            
        