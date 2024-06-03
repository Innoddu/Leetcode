# 695. Max Area of Island
def maxAreaOfIsland(grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        maxIsland = 0
        visited = set()
        def bfs(r, c):
            if r not in range(rows) or \
                c not in range(cols) or \
                grid[r][c] == 0 or \
                (r, c) in visited:
                return 0

            visited.add((r, c))
            direction = [[0,1], [0, -1], [1,0],[-1,0]]
            return (1 + bfs(r + 1, c) + bfs(r - 1, c) + bfs(r, c + 1) + bfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxIsland = max(maxIsland, bfs(r, c))
 

        return maxIsland
