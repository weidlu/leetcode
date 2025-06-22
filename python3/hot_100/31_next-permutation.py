from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while nums[i] >= nums[i + 1] and i >= 0:
            i -= 1
        if i >= 0:
            # 找到一个合法的 i，继续找 i到 n-1之间 大于 nums[i]的最小的数
            # 因为这个数组现在必定是从 i->n的增序 所以就是要找到大于nums[i]的第一个数
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    # Example usage:
    nums = [1, 1]
    solution = Solution()
    solution.nextPermutation(nums)
    print(nums)  # Expected output: [1, 3, 2] (the next permutation)
