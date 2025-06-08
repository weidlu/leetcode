from ctypes.wintypes import tagSIZE
from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicate elements to avoid duplicate triplets
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second element
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


if __name__ == '__main__':
    # Example usage:
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)  # Expected output: [[-1, -1, 2], [-1, 0, 1]] or similar combinations
