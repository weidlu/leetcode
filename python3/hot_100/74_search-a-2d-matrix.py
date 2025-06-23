from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        target_row = -1
        for i in range(m):
            if matrix[i][n-1] >= target:
                target_row = i
                break
        if target_row == -1:
            return False

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[target_row][mid]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False  # 没找到


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    sol = Solution()
    result = sol.searchMatrix(matrix, target)
    print(f"searchMatrix(matrix, {target}) = {result}")
