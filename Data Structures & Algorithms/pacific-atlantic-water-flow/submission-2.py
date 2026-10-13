class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        pacific = set()
        atlantic = set()  

        for i in range(rows):
            pacific.add((i,0))
            atlantic.add((i,cols-1))
        
        for i in range(cols):
            pacific.add((0,i))
            atlantic.add((rows-1,i))
        
        common = pacific & atlantic

        for row in range(rows):
            for col in range(cols):
                present_pac = False
                present_atl = False
                q = deque([(row, col)])
                visited = {(row, col)}
                while q:
                    r, c = q.popleft()
                    if present_pac and present_atl:
                        return
                    if (r,c) in pacific:
                        present_pac = True
                        pacific.add((r,c))
                    if (r,c) in atlantic:
                        present_atl = True
                        atlantic.add((r,c))

                    if present_pac and present_atl:
                        common.add((row, col))
                        break
                    
                    for dr, dc in directions:
                        x = r + dr
                        y = c + dc
                        if 0 <= x < rows and 0 <= y < cols and heights[x][y] <= heights[r][c] and (x,y) not in visited:
                            visited.add((x, y))
                            q.append((x,y))
                
                if present_pac and present_atl:
                    common.add((row, col))
        
        return list(common)



        

        
