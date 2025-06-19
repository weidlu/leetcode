from typing import List

# ---
#
# ### 🔹 Q1: 为什么二分查找插入位置时循环条件是 `i <= j`，而不是 `i < j`？
#
# **A:**
# 使用 `i <= j` 可以确保在 `i == j` 的情况下仍会进入循环，从而判断最后一个元素是否满足条件。如果使用 `i < j`，当 `i == j` 时就会跳出循环，导致最后一个元素未被处理，可能出现错误结果。
#
# 🔍 例如：
#
# ```python
# nums = [1]
# target = 1
# ```
#
# * 若用 `while i < j`，则根本不会检查 `nums[0]`，因为 `i == j == 0`，直接跳出循环；
# * 使用 `while i <= j`，就能正确判断 `nums[0] == target` 并返回下标。
#
# ---
#
# ### 🔹 Q2: 为什么循环结束后返回的是 `i`，而不是 `j`？
#
# **A:**
# 在插入位置问题中，循环退出时条件是 `i > j`。此时，`i` 正好指向第一个大于等于 `target` 的位置，也就是应插入的位置。
#
# 📌 理解关键：
#
# * 二分查找不断缩小范围；
# * 每次比较后若 `nums[mid] < target`，则 `i = mid + 1`；
# * 若 `nums[mid] > target`，则 `j = mid - 1`；
# * 最终退出循环时，`i` 就是应插入的位置。
#
# 🔍 例如：
#
# ```python
# nums = [1, 3, 5, 6]
# target = 4
# ```
#
# 执行完后：
#
# * `i = 2`
# * `j = 1`
# * 插入位置就是下标 2
#
# ---
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            if nums[mid] > target:
                j = mid - 1
        return i


if __name__ == "__main__":
    # Example usage:
    nums = [1, 3, 5, 6]
    target = 5
    solution = Solution()
    result = solution.searchInsert(nums, target)
    print(result)  # Expected output: 2
