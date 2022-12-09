from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            # 左侧有序
            elif nums[0] <= mid_num:
                if nums[0] <= target < mid_num:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右侧有序
            elif nums[0] > mid_num:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    left = s.search(nums, 0)
    print(left)
