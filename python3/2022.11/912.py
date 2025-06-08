import random

import math
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums and nums[0] == 2:
            for n in nums:
                if n != 2:
                    break
                else:
                    return nums
        random.shuffle(nums)
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums, lo, hi):
        if lo >= hi:
            return
        # nums[lo..p - 1] <= nums[p] < nums[p + 1..hi]
        p = self.partition(nums, lo, hi)
        self.sort(nums, lo, p - 1)
        self.sort(nums, p + 1, hi)

    def partition(self, nums: List[int], lo: int, hi: int):
        pivot = nums[lo]
        # 我这里把 i, j 定义为开区间，同时定义：
        # [lo, i) <= pivot；(j, hi] > pivot
        i, j = lo + 1, hi
        # 当 i > j 时结束循环，以保证区间 [lo, hi] 都被覆盖
        while i <= j:
            while i < hi and nums[i] <= pivot:
                i += 1
            # 此while 结束时恰好 nums[i] > pivot
            while j > lo and nums[j] > pivot:
                j -= 1
            # 此while 结束时恰好 nums[j] <= pivot
            # 此时[lo, i) <= pivot & & (j, hi] > pivot
            if i >= j:
                # 进循环之前符合i>=j的条件，循环中i++ j--之后可能不满足这个条件了，所以需要再检查一下
                # 如果不满足需要退出
                break
            self.swap(nums, i, j)

        self.swap(nums, lo, j)
        return j

    def less(self, nums, i, j):
        return nums[i] - nums[j] < 0

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    s = Solution()
    s.sortArray(nums)
    print(nums)
