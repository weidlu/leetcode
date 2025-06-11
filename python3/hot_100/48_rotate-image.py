from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        n = len(matrix)
        index = 0
        for i in range(n // 2):
            # 一圈一圈的做
            for j in range(i, n - i - 1):
                # 每一圈需要交换的下标的范围
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
                matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]


if __name__ == '__main__':
    # Example usage:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution = Solution()
    solution.rotate(matrix)
    print(matrix)  # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # output should be:
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]

    #  i -> j

    # another example
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    solution.rotate(matrix)
    print(matrix)
    # output should be:
    # [[15, 13, 2, 5],
    #  [14, 3, 4, 1],
    #  [12, 6, 8, 9],
    #  [16, 7, 10, 11]]

    # 一圈一圈的做 直到矩阵的中心
