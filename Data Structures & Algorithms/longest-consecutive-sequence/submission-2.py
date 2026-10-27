class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # nums = [2,3,4,5]
        # Output = 4
        # sort = n log n
        # neither sort will work neither 2 pointer will work
        s = set(nums)
        longest = 0
        for num in nums:
            counter = 0
            if num-1 not in s:
                # check the streak
                while num in s:
                    counter += 1
                    num +=1
            longest = max(longest,counter)
        return longest
                

                

