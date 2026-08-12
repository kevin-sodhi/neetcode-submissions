import heapq     # importing for Heap PQ
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)         # O(n)
        # nums = [1, 1, 1, 2, 2, 3]
        # counter == Counter({1: 3, 2: 2, 3: 1})
        # 1:3 == > key(number) : values(frequency in this)
        # sorting them through values   O(nlogn) sortingg
        # we will use a tupple with (freq,key) and add it to the PQ heap
        # so the heap will have tuples adding to the limit of (K)
            # and the tuples are in order (freq,key) and the heap will sort them 
            # according to the highest freq : 
            #               (1,3)       lowest freq 
            #              /     \
            #            (2,2)    (3,1)

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val,key)) # push
            else: 
                heapq.heappushpop(heap, (val,key))     # push then pop
                # when the new tuple will add the old and the less frequest one will pop
        return [h[1] for h in heap] 
        
        # (freq, number)
        # (val, key)
        # heap = [(2, 2), (3, 1)]
        # h[0] is the frequency
        # h[1] is the actual number (the element from nums)


            

            

        
        