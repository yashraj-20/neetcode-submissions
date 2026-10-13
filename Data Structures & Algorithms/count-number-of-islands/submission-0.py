class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    island += 1

                    queue = deque([(row, col)])

                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in direction:
                            nx = x + dx
                            ny = y + dy
                        
                            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1"):
                                grid[nx][ny] = "0"

                                queue.append((nx,ny))
        
        return island

