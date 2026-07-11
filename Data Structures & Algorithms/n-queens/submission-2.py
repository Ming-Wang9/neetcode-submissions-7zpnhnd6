class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        colset, posdia, negdia = set(), set(), set()
        board = [["."] * n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c not in colset and (r+c) not in posdia and (r-c) not in negdia:
                    board[r][c] = "Q"
                    colset.add(c)
                    posdia.add(r+c)
                    negdia.add(r-c)
                    backtrack(r+1)
                    colset.remove(c)
                    posdia.remove(r+c)
                    negdia.remove(r-c)
                    board[r][c] = "."
        backtrack(0)
        return res