class Solution:
    def isPalindrome(self, s: str) -> bool:
        cStr = ""
        for c in s:
            if c.isalnum():
                cStr += c.lower()

        i = 0
        j = len(cStr) - 1

        while i < j:
            if cStr[i] != cStr[j]:
                return False
            i += 1
            j -= 1

        return True
        