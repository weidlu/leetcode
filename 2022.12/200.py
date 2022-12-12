from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandNum = 0
        rl, cl = len(grid), len(grid[0])
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == '1':
                    islandNum += 1
                    self.dfs(grid, i, j)
        return islandNum

    def dfs(self, grid: List[List[str]], i: int, j: int):
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右
        rl, cl = len(grid), len(grid[0])
        if i < 0 or i >= rl or 0 > j or j >= cl:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for d in direct:
            self.dfs(grid, i + d[0], j + d[1])
        return


if __name__ == "__main__":
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    s = Solution()
    num = s.numIslands(grid)
    print(num)

