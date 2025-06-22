from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if not nums or k == 0:
            return []
        result = []
        dq = deque()
        for i, v in enumerate(nums):
            # 出队
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 当前元素入队后任需要保持队列单调
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq.append(i)
            # i过了第一个窗口位置后就可以加入答案了
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

    # dq = deque()
    # res = []
    # for i, v in enumerate(nums):
    #     # 1) 弹出过期下标
    #     if dq and dq[0] < i - k + 1:
    #         dq.popleft()
    #     # 2) 保持队内单调：把小于 v 的都删掉
    #     while dq and nums[dq[-1]] < v:
    #         dq.pop()
    #     dq.append(i)
    #     # 3) 记录答案
    #     if i >= k - 1:
    #         res.append(nums[dq[0]])
    # return res


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if k > len(nums):
        k = len(nums)
    result = []

    last_max = max(nums[:k])
    result.append(last_max)

    for i in range(1, len(nums) - k + 1):
        out_num = nums[i - 1]
        in_num = nums[i + k - 1]
        if in_num >= last_max:
            last_max = in_num
        elif out_num != last_max:
            pass
        else:
            last_max = max(nums[i:i + k])
        result.append(last_max)
    return result


if __name__ == "__main__":
    # Example usage:
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # nums = [3, 1, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)  # Expected output: [3, 3, 5, 5, 6, 7]
