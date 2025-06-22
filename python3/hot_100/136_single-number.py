from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result

if __name__ == "__main__":
    # Example usage:
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    result = solution.singleNumber(nums)
    print(result)  # Expected output: 4 (the number that appears only once)
