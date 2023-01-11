class Insertion(object):
    """
    插入排序：让局部逐渐有序，每次向前遍历找到当前元素在局部有序的部分里的相对位置。
    """

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        length = len(self.nums)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if self.less(j, j - 1):
                    self.swap(j, j - 1)
        return

    def less(self, _i, j):
        return self.nums[_i] < self.nums[j]

    def swap(self, _i, j):
        tmp = self.nums[_i]
        self.nums[_i] = self.nums[j]
        self.nums[j] = tmp


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    i = Insertion(nums)
    i.sort()
    print(i.nums)
