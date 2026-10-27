class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix idx = i-1
        # postfix idx = i+1
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res





        
        '''
        O(n^2) solution
        # nums = [1,2,4,6]
        arr = []
        i = 0
        while i < len(nums): 
            num = nums[i] # 1
            index = i
            nums.pop(i) # O(n)
            result = math.prod(nums) # O(n)
            arr.append(result)
            nums.insert(index, num) # O(n)
            i+=1
        return arr
        '''
            