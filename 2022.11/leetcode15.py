class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        start = -1
        while start < len(nums) - 1:
            start += 1
            cur = nums[start]
            _re = self.twoSum(nums[start + 1:], -cur)
            for r in _re:
                r.append(cur)
                result.append(r)
            while start < len(nums) - 1 and cur == nums[start + 1]:
                start += 1
        return result

    def twoSum(self, _nums, k):
        nums = _nums
        nums.sort()
        result = []
        low = 0
        high = len(nums) - 1
        # lo.....high
        while low < high:
            left, right = nums[low], nums[high]
            if nums[low] + nums[high] < k:
                low += 1
            elif nums[low] + nums[high] > k:
                high -= 1
            else:
                a = [nums[low], nums[high]]
                result.append(a)
                while low < len(nums) - 1 and nums[low] == left:
                    low = low + 1
                while high > 0 and nums[high] == right:
                    high = high - 1
        return result


if __name__ == "__main__":
    nums = [1, 2, -2, -1]
    s = Solution()
    re = s.threeSum(nums)
    print(re)
