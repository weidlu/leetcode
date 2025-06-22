from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums) // 2)]


if __name__ == "__main__":
    # Example usage:
    nums = [3, 2, 3]
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)  # Expected output: 3 (the majority element)
