import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 优先队列（小顶堆）
        p = MaxHeap(k+1)
        for n in nums:
            p.insert(n)
            if p.size() > k:
                p.peekAndDel()
        return p.peek()


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return int(i / 2)


class MaxHeap(object):
    def __init__(self, capacity):
        self.pq = [0 for i in range(capacity + 1)]
        self.N = 0
        self.cap = capacity

    def size(self):
        return self.N

    def insert(self, x):
        self.N += 1
        self.pq[self.N] = x
        self.swim(self.N)
        return

    def peekAndDel(self) -> int:
        # 最大节点和最小节点互换
        _max = self.pq[1]
        self.exch(1, self.N)
        self.pq[self.N] = 0
        self.N -= 1
        self.sink(1)
        return _max

    def peek(self):
        return self.pq[1]

    def swim(self, k):
        """
        上浮
        :param k:
        :return:
        """
        # 如果父节点存在且
        while parent(k) >= 1 and self.less(parent(k), k):
            self.exch(k, parent(k))
            self.swim(parent(k))
        return

    def sink(self, k):
        """
        下沉
        :param k:
        :return: None
        """
        # 存在下一层节点
        while 2 * k <= self.size():
            # 子节点中的较大的一个
            j = 2 * k
            if j < self.size() and self.less(j, j + 1):
                j += 1
            # 如果父节点大于子节点
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j
        return

    # 交换
    def exch(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp
        return

    def less(self, i, j):
        return self.pq[i] - self.pq[j] > 0


if __name__ == "__main__":
    # _maxHeap = MaxHeap(capacity=10)
    # _maxHeap.insert(2)
    # _maxHeap.insert(3)
    # _maxHeap.insert(6)
    # _maxHeap.insert(1)
    # print(_maxHeap.pq)
    # _maxHeap.delMax()
    # print(_maxHeap.pq)
    s = Solution()
    # [3,2,1,5,6,4] 2
    nums = [3, 2, 1, 5, 6, 4]
    kMax = s.findKthLargest(nums, 2)
    print(kMax)
