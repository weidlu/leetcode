from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in map and map[target - nums[i]] != i:
                return [i, map[target - nums[i]]]

if __name__ == "__main__":
    n = [3, 2, 4]
    s = Solution()
    print(s.twoSum(n, 6))
