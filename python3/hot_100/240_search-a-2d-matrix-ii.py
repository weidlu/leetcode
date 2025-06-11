from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        row_index = row_len - 1
        col_index = 0
        while row_index >= 0 and col_index <= col_len - 1:
            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] < target:
                col_index += 1
            else:
                row_index -= 1


if __name__ == '__main__':
    # Example usage:
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
        [60, 61, 62, 63]
    ]
    target = 3
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    print(result)  # Expected output: True