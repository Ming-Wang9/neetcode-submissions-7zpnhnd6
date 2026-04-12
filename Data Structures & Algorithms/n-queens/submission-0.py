class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        poDi = set()
        NeDi = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                board_copy = [''.join(row) for row in board]
                res.append(board_copy)
                return 
            for c in range(n):
                if c in col or (r+c) in poDi or (r-c) in NeDi:
                    continue
                col.add(c)
                poDi.add(r+c)
                NeDi.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                col.remove(c)
                poDi.remove(r+c)
                NeDi.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res