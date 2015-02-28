class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        n, m = len(grid[0]), len(grid)
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        print grid

        for j in range(1, n):
            for i in range(1, m):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1])
        print grid

        return grid[m - 1][n - 1]

s = Solution()

print s.minPathSum([[1,2],[1,1]])

