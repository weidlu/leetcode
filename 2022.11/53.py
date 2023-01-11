from typing import List


def dpSolution(nums: List[int]) -> int:
    maxR = -999999999
    """
    动态规划，主要考虑dp的定义
    dp[i]表示以nums[i]结尾的连续子数组和最大值
    dp[i] = max(dp[i-1], dp[i-1]+nums[i])
    """
    dp = [-99999999] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    for r in dp:
        maxR = max(r, maxR)
    return maxR


def slideWindow(nums: List[int]) -> int:
    """
    滑动窗口法，主要需要思考：
    1.何时扩大、缩小窗口
    2.何时更新答案"""
    length = len(nums)
    maxSum, left, right = 0, 0, 0
    windowSum = 0
    while right < length:
        windowSum += nums[right]
        right += 1
        maxSum = max(maxSum, windowSum)

        while windowSum < 0:
            windowSum -= nums[left]
            left += 1
            maxSum = max(maxSum, windowSum)
    return maxSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return slideWindow(nums)


if __name__ == "__main__":
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    r = s.maxSubArray(n)
    print(r)
