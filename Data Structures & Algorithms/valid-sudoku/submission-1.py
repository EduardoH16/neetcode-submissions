class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, l in enumerate(board):
            numSet = set()
            for s in l:
                if s == ".":
                    continue
                if s in numSet:
                    return False
                numSet.add(s)

        for i in range(9):
            numSet = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in numSet:
                    return False
                numSet.add(board[j][i])

        arr_set = [[set(), set(), set()] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                set_row = i//3
                set_col = j//3
                if board[i][j] == ".":
                    continue
                if board[i][j] in arr_set[set_row][set_col]:
                    return False
                arr_set[set_row][set_col].add(board[i][j])
        return True
            
         