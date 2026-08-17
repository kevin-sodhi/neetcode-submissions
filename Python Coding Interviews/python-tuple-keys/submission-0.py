from typing import List, Set, Tuple

'''
[[1, 0, 1], (1,1) = [][0]
 [0, 1, 0], 
 [1, 0, 1]]
'''

def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    set_pair = set()
    for r in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[r][j] == 1:
                set_pair.add((r,j))
    return set_pair
        



# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
