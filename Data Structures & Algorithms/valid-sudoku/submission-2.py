class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen =set()
            for i in range(9):
                if board[r][i] == '.':
                    continue
                if board[r][i] in seen:
                    return False
                seen.add(board[r][i])

        for c in range(9):
            seen = set()
            for j in range(9):
                if board[j][c] == '.':
                    continue
                if board[j][c] in seen:
                    return False
                seen.add(board[j][c])

        for row in range(0,9,3):
            for col in range(0,9,3):
                seen=set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        return True






