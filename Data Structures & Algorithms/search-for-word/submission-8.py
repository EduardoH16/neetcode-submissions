class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(r, c, i):
            found = False
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            curr_char = board[r][c]
            if curr_char == ".":
                return False
            if curr_char == word[i]:
                board[r][c] = "."
                found = (backtrack(r - 1, c, i + 1) or 
                        backtrack(r + 1, c, i + 1) or 
                        backtrack(r, c - 1, i + 1) or 
                        backtrack(r, c + 1, i + 1))
    
            board[r][c] = curr_char
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False