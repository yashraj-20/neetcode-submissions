class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for row in range(rows):
            for col in range(cols):
                area = 0
                if grid[row][col] == 1:
                    grid[row][col] = 0

                    queue = deque([(row, col)])

                    while queue:
                        x, y = queue.popleft()
                        area += 1
                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy

                            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1):
                                grid[nx][ny] = 0
                                queue.append((nx, ny))
                    
                    max_area = max(max_area, area)
        
        return max_area
