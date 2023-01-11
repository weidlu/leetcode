class Selection(object):
    """
    选择排序
    时间复杂度O(N^2)
    """
    def __init__(self, nums):
        """
        :param nums: int list
        """
        self.nums = nums

    def sort(self):
        length = len(self.nums)
        for _i in range(length):
            minIndex = _i
            for j in range(_i, length):
                if not self.less(minIndex, j):
                    minIndex = j
            self.swap(_i, minIndex)
        return

    def less(self, _i, j):
        return self.nums[_i] < self.nums[j]

    def swap(self, _i, j):
        tmp = self.nums[_i]
        self.nums[_i] = self.nums[j]
        self.nums[j] = tmp


if __name__ == "__main__":
    nums = [3, 5, 7, 1, 8, 3, 6, 8]
    i = Selection(nums)
    i.sort()
    print(i.nums)
