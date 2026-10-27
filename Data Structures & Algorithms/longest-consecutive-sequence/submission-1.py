class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # nums = [2,3,4,5]
        # Output = 4
        # sort = log n
        # neither sort will work neither 2 pointer will work
        s = set()
        longest = 0
        for num in nums:
            s.add(num)
        for num in nums:
            counter = 0
            if num-1 not in s:
                #check if there is a sequence from num+1
                # num, num+1, num+2, num+3
                while num in s:
                    #check if there is a sequence from num+1
                    counter += 1
                    num +=1
            longest = max(longest,counter)
        return longest
                

