class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # adding the t list in map
        t_map = {}
        for t_chr in t:
            if t_chr in t_map: t_map[t_chr] += 1
            else: t_map[t_chr] = 1
        
        min_len = float('inf')
        start_idx = -1
        window_char = {}
        l = 0
        have = 0 
        need = len(t_map) # the req char we need to make the substring valid

        for r in range(len(s)):
            # add the chr in window_char map
            if s[r] not in window_char: 
                window_char[s[r]] = 1
            else: 
                window_char[s[r]] += 1

            if s[r] in t_map and window_char[s[r]] == t_map[s[r]]:
                have += 1
            
            while have == need:
                window = r-l+1
                if window < min_len:
                    min_len = window
                    start_idx = l # the index where we will get our substring started
                
                # now we are shrinking the window from left side 
                if s[l] in t_map and window_char[s[l]] == t_map[s[l]]:
                    have -= 1
                
                if window_char[s[l]] == 1:
                    del window_char[s[l]]
                else:
                    window_char[s[l]] -= 1
                l+=1
        
        if min_len == float('inf'):
            return ""
        else:
            return s[start_idx:start_idx+min_len]
        







        
        
        
        
        
        
        '''
        My failed Approch : 

        t = Counter(t)
        left = 0
        right = 0
        min_len = float('inf')
        start = 0
        while right<len(s):
            if s[right] in t:
                # decrement the founded element
                t[s[right]] -= 1
                # now we will check if our window is valid by checking all the elements in t <0
                while all(value <= 0 for value in t.values()):
                    # find the shortest window size
                    window = right-left+1
                    if window < min_len:
                        start = left
                    # now we have to shrink the window
                    # if while decreasing the left we find a chr that is in t we increment it 
                    if s[left] in t:
                        t[s[left]] += 1
                    left+=1
                    valid = all(value <= 0 for value in t.values())
            right +=1
        if min_len == float('inf'):
            return ""
        return s[start:start+min_len]

        Goal: return the shortest substring of s
        "OUZODYXAZV"
        "0123456789"
        My approch:
            t = "XYZ"
            lets put this t in a set()
            curr_window = 0 
            left = 0
            while left < len(s):
                if s[left] in set():
                    # we foumd our left pointer now we need to start a window
                    # starting from left we will increment 
                    # but we have to make sure if left+1 is not in set maybe
                    # left+2 can be inset untill we find the next elemt that is in the set
                    then we can have a while loop untill we find the chr in S or till the end 

        '''
        