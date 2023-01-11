from typing import List


class Solution:
    """螺旋矩阵"""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m_start = 0
        m_end = len(matrix)
        n_start = 0
        n_end = len(matrix[0])

        m_curr = 0
        n_curr = 0

        res = []

        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_count = 0

        while m_start != m_end and n_start != n_end:
            _dir = d_count % 4
            if m_start <= m_curr < m_end and n_start <= n_curr < n_end-1:
                res.append(matrix[m_curr][n_curr])
                m_curr = m_curr + direct[_dir][0]
                n_curr = n_curr + direct[_dir][1]
            else:
                if direct[_dir][1] == 1:
                    m_end -= 1
                elif direct[_dir][1] == -1:
                    m_start += 1

                if direct[_dir][0] == 1:
                    n_end -= 1
                elif direct[_dir][0] == -1:
                    n_end += 1

                d_count += 1

                m_curr = m_curr + direct[d_count % 4][0]
                n_curr = n_curr + direct[d_count % 4][1]
                continue
        return res


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s = Solution()
    res = s.spiralOrder(matrix)
    print(res)
