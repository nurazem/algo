class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        # if len(matrix) == 1:
        #     for m in matrix[0]:
        #         if m == 0:
        #             return [0]*len(matrix[0])

        r, c = len(matrix), len(matrix[0])
        rows= []
        columns = []

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.append(i)
                    rows.append(j)
        print (rows, columns)
        for i in range(r):
            for j in range(c):
                if j in rows or i in columns:
                    matrix[i][j] = 0

        return matrix

print Solution().setZeroes([[0],[1]])
