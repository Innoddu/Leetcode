def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(x , y, visit):
            visit.add( (x,y) )
            directions = [[-1,0], [1,0], [0, 1], [0, -1]]
            for dx, dy in directions:
                n_x, n_y = x+dx, y+dy
                if 0 <= n_x < rows and 0 <= n_y < cols and (n_x, n_y) not in visit and heights[n_x][n_y] >= heights[x][y]:
                    dfs(n_x, n_y, visit)
        for c in range(cols):
            dfs(0, c, pac )
            dfs(rows - 1, c, atl)
        
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        
        for r in range(rows):
            for c in range(cols):
                if ( r, c ) in pac and (r,c)in atl:
                    res.append([r,c])
        return res
