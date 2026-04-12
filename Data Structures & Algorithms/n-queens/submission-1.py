class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset,poset,neset=set(),set(),set()
        res = []
        board =[['.']*n for i in range(n)]
        def backtrack(r):
            if r==n:
                boardcopy = [''.join(row) for row in board]
                res.append(boardcopy)
                return 
            for c in range(n):
                if c in colset or (r+c) in poset or (r-c) in neset:
                    continue
                colset.add(c)
                poset.add(r+c)
                neset.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                colset.remove(c)
                poset.remove(r+c)
                neset.remove(r-c)
                board[r][c] = '.'
        backtrack(0)
        return res
                

