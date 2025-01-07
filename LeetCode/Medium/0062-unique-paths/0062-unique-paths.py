class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[ 0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1

        for row in range(m):
            for col in range(n):
                if col-1 >= 0:
                    matrix[row][col] += matrix[row][col-1]
                if row-1 >= 0:
                    matrix[row][col] += matrix[row-1][col]
        
        return matrix[m-1][n-1]