class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        boxset = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                idx = r//3*3+c//3
                if val in rowset[r] or val in colset[c] or val in boxset[idx]:
                    return False
                rowset[r].add(val)
                colset[c].add(val)
                boxset[idx].add(val)
        return True