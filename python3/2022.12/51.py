import copy
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:

        def isValid(board: List[str], row: int, col: int) -> bool:
            n = len(board)
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False

            # i    range(row - 1, -1, -1)
            # j    range(col + 1, n, 1)
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[i][j] == 'Q':
                    return False

            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            return True

        def replace_index(s: str, index: int, replace: str):
            return s[:index] + replace + s[index + 1:]

        def backtrack(board: List[str], row: int):
            if row == len(board):
                t = copy.deepcopy(track)
                self.res.append(t)
                return

            n = len(board[row])
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                track[row] = replace_index(board[row], col, 'Q')
                backtrack(board, row + 1)
                track[row] = replace_index(board[row], col, '.')

        track = ['.' * n for _ in range(n)]
        backtrack(track, 0)
        return self.res


if __name__ == "__main__":
    s = Solution()
    s.solveNQueens(4)

    print(s.res)
