# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # sort using key
        # Return a list of lists showing the state of the array after each insertion.
        res = []
        length = len(pairs)
        if len(pairs) == 0:
            return res
        res.append(pairs.copy())
        for i in range(1,length):
            j = i-1
            while (j>=0 and pairs[j].key > pairs[j+1].key):
                #swap
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            res.append(pairs.copy())
        return res
            