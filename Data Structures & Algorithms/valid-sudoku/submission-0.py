class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        we can go through each row and col and check 1-9 with no duplicates
            we can go 3x3 grid to check 1-9 with no dublicates
        
        Row = board
        col = board[0]
        how can we check dups = we can use a set()
            if the num is not in set then add:
                if it is in set then return FALSE
        '''
        # Row Validation
        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
        # col Validation
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
        # grid validation
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        num = board[r][c]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        
        return True
            

        