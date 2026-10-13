class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_arr = list(word)
        word_len = len(word_arr)
        cols = len(board[0])
        rows = len(board)

        def backtracking(r, c, i):
            # Word completely matched
            if i == word_len:
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Character doesn't match
            if board[r][c] != word[i]:
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 directions
            found = (
                backtracking(r + 1, c, i + 1) or
                backtracking(r - 1, c, i + 1) or
                backtracking(r, c + 1, i + 1) or
                backtracking(r, c - 1, i + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found
        # Try every cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True

        return False