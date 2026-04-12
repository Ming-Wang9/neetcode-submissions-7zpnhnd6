class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Check 3×3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        return True
