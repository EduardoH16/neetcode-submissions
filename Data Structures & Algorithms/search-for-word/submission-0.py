class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def backtrack(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or row >= ROWS or col < 0 
                or col >= COLS or board[row][col] != word[i]): 
                return False
            
            c = board[row][col]
            board[row][col] = "."
            i += 1
            found = (backtrack(row - 1, col, i) or 
                    backtrack(row + 1, col, i) or
                    backtrack(row, col - 1, i) or
                    backtrack(row, col + 1, i))
            
            board[row][col] = c
            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False