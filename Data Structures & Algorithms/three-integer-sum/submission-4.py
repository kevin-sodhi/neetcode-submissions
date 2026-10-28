class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        # -nums[i] = nums[j] + nums[k]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while j < k: # j = left* and k = right*
                curr_sum = nums[j] + nums[k]
                if curr_sum == target: # curr_sum = target --> triplet
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                elif curr_sum < target: # curr_sum < target --> inc left pointer 
                    j += 1
                else: # curr_sum > target --> dec right pointer
                    k -= 1 
        return res
    
    