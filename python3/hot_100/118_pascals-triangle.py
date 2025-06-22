from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp.append(row)
        return dp


if __name__ == "__main__":
    # Example usage:
    numRows = 5
    solution = Solution()
    result = solution.generate(numRows)
    print(result)  # Expected output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
