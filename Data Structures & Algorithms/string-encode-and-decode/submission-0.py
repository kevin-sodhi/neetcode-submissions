class Solution:
    '''
    # EDGE CASE :
    #   -> if we use a delimmiter for making the split in the string then 
    #      any word that has the same delimmiter can mess up our result:
    #      String_list = [kevin, #jasmine, mom, dad]
           encoded = kevinjasm#inemomdad no way to find out how to split
           encoded_with_"#" = #kevin#jasm#ine#mom#dad
           decoded = [kevin, jasm, ine, mom, dad] ## decode != encoded
           SOLUTION = we use delimiter "len(string[i]) and #"
                      len will tell us how many words does the string has after '#'
    '''

    def encode(self, strs: List[str]) -> str:
        string = ""
        for ch in strs:
            string += str(len(ch)) + "#" + ch
        return string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            # we will get [len()#]
            length = int(s[i:j]) # we got the integer length
            string = s[j+1:j+1+length]
            res.append(string)
            i = j + 1 + length # we need to move i to the beginning of the next encoded word.
        return res

    '''
    Character:  5  #  k  e  v  i  n  3  #  m  o  m  3  #  d  a  d
    Index:      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
        i = j + 1 + length # we need to move i to the beginning of the next encoded word.
        At Loop 1: 
            i = 0
            after inserting in the list 
            i = 7
    '''



        