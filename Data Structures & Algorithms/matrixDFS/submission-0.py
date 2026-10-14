class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
         # USING DFS WITH BACKTRACKING 
         return self.dfs(grid,0,0,set())
    
    def dfs(self,grid,r,c,visited):
        ROWS = len(grid)
        COLS = len(grid[0])
        # Base Case 1
        if (
            min(r,c) < 0 or
            r == ROWS or c == COLS or 
            (r,c) in visited or grid[r][c] == 1
        ):
            return 0
        # Base Case 2
        if r == ROWS-1 and c == COLS-1:
            return 1
        
        visited.add((r,c))
        count = 0 
        count += self.dfs(grid,r+1,c,visited)
        count += self.dfs(grid,r-1,c,visited)
        count += self.dfs(grid,r,c+1,visited)
        count += self.dfs(grid,r,c-1,visited)

        visited.remove((r,c))
        return count


        





        