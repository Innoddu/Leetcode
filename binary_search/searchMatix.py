def searchMatrix(matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = cols - 1
        left = 0
        right = c
        while r < rows:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] >= target:
                # searching.... current rows
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False

        
        return False
