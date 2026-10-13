class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        pos_daig = set()
        neg_daig = set()

        board = [["."] * n for _ in range(n)]

        def backtracking(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols:
                    continue
                if col - row in pos_daig:
                    continue
                if col + row in neg_daig:
                    continue
                
                board[col][row] = "Q"
                cols.add(col)
                pos_daig.add(col - row)
                neg_daig.add(col + row)

                backtracking(row+1)
                board[col][row] = "."
                cols.remove(col)
                pos_daig.remove(col - row)
                neg_daig.remove(col + row)
            
        backtracking(0)
        return result
            