from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 1) 初始化：多源入队 + 统计 fresh
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # 如果没有 fresh，直接 0 分钟
        if fresh == 0:
            return 0

        minutes = 0
        # 2) BFS 分层
        while queue:
            size = len(queue)
            # 本层是否腐烂了新鲜橘子
            infected = False
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
                        infected = True
            # 只有这一分钟确实有传播，才算一分钟
            if infected:
                minutes += 1

        # 3) 结果判断
        return minutes if fresh == 0 else -1
