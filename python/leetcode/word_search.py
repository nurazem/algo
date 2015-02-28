
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        i, j = 0, 0 # i -> rows, j -> columns
        n, m = len(board), len(board[0])
        while i < n:
            while j < m:
                print i
                print j
                if word[0] == board[i][j]:
                    visited = {(i, j): True}
                    w = 1 # letter index
                    neighbors = self.neighbors(i, j, n, m)
                    print neighbors
                    while words[w] in neighbors and words[w] not in visited:
                        if w == len(word):
                            return True

                        pair = neighbors[words[w]]
                        neighbors = self.neighbors(pair[0], pair[1], n, m)
                        w += 1

                j += 1
            i += 1

        return False

    def neighbors(self, i, j, n, m, board):
        neighbors = {}
        if i != 0:
            neighbors[board[i - 1][j]] = (i - 1, j)
        if j != 0:
            neighbors[board[i][j - 1]] = (i, j - 1)
        if i != n - 1:
            neighbors[board[i + 1][j]] = (i + 1, j)
        if j != m -1:
            neighbors[board[i][j + 1]] = (i, j + 1)
        print neighbors
        return neighbors


Solution().neighbors(0, 0, 3, 4, [["ABCE"], ["SFCS"], ["ADEE"]])
#print Solution().exist([["ABCE"], ["SFCS"], ["ADEE"]], 'ABCCED')
