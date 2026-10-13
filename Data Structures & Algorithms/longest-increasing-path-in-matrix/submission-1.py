class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}
        def df(x, y):
            final = 1
            if (x,y) in dp:
                return dp[(x,y)]
            for dx, dy in direction:
                nx = dx + x
                ny = dy + y
                if 0<=nx<rows and 0<=ny<cols:
                    if matrix[nx][ny] > matrix[x][y]:
                        final = max(final, 1+df(nx,ny))
            dp[(x,y)] = final
            return final
        ans = 0

        for i in range(rows):
            for j in range(cols):
                ans = max(ans, df(i, j))

        return ans

