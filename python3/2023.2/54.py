from typing import List


class Solution:
    def spiral(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, columns = len(matrix), len(matrix[0])
        order = []

        visited = [[False] * columns for _ in range(rows)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        total = rows * columns
        direction_index = 0
        for i in range(total):
            order.append(matrix[row][column])
            visited[row][column] = True
            next_row, next_column = row + directions[direction_index][0], column + directions[direction_index][1]
            if not (0 <= next_row < rows and 0 <= next_column < column and not visited[next_row][next_column]):
                direction_index = (direction_index + 1) % 4
                row += directions[direction_index][0]
                column += directions[direction_index][1]
        return order


if __name__ == "__main__":
    s = Solution()
    m = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    print(s.spiral(m))

