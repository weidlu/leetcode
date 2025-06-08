# result = []
#
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
#
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择
from typing import List


class Solution:
    _tracks = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        t = []
        visit = [False for _ in range(len(nums))]
        self.back_track(nums, t, visit)
        return self._tracks

    def back_track(self, nums: List[int], track: List[int], visited: List[bool]):
        if len(track) == len(nums):
            self._tracks.append(track[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            track.append(nums[i])
            visited[i] = True
            self.back_track(nums, track, visited)
            track.pop()
            visited[i] = False


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == "__main__":
    _input = [1, 2, 3]
    s = Solution()
    res = s.permute(_input)
    print(res)
