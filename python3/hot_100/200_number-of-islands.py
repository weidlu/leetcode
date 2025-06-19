from collections import deque
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    queue = deque([(i, j)])
                    grid[i][j] = "0"
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                queue.append((nx, ny))
        return island_count

    def numIslands1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0

        def dfs(i: int, j: int):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)
        return island_count


if __name__ == "__main__":
    # Example usage:
    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)  # Expected output: 3
