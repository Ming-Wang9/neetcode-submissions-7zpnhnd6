class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
       

        def dfs (r,c):
            if (r<0 or c<0 or
                r >= rows or c >= cols or
                board[r][c] != 'O'):
                return 
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # find the 'O' on the boundry side, and do dfs 
        for r in range(rows):
            for c in range(cols):
                if ((r==0 or r == rows -1 or
                    c == 0 or c == cols -1) and 
                    board[r][c] == 'O'):
                    dfs(r,c)

        # after change the unsurrounded 'O' to temp value,
        # then loop through everything and mark it to 'X' 
        # and change the temp value back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        

