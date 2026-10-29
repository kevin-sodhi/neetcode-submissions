class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        pairs = {')':'(', ']':'[','}':'{'}
        for i in s:
            if i in "({[":
                stk.append(i)
            else:
                if not stk:
                    return False
                ele = stk.pop()
                if ele != pairs[i]:
                    return False

        return len(stk)==0
        