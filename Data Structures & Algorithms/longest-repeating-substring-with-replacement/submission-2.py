class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        the first think we should do is to find the most freq letter from the s
        '''
        left = 0
        result = 0
        count = {}
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            max_freq = max(count.values())
            while (right-left+1) - max_freq > k:
                # removing the chr from window
                count[s[left]] -= 1
                # shrink the window
                left += 1
            result = max(result,(right-left+1))
        return result
                







        


        

         


