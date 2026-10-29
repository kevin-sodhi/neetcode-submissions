class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stk = []
        pairs = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i == '[' or i == '{' or i =='(':
                stk.append(i)
            else:
                if not stk:
                    return False
                ele = stk.pop()
                if ele != pairs[i]:
                    return False
        return len(stk) == 0
        