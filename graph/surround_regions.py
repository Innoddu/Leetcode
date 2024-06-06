def solve(board):
        """
        Do not return anything, modify board in-place instead.
        """
        # filpped
        # 1. not border
        # 2. surrounding region which is X
        rows = len(board)
        cols = len(board[0])

        def findBorder(r,c):
            if r < 0 or r ==rows or c < 0 or c == cols or board[r][c] != "O":
                return
            board[r][c] = "E"

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                findBorder(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1]) or c in[0, cols - 1]:
                    findBorder(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "E":
                    board[r][c] = "O"

        return board
