class LRUCache(object):
    """
    LRU缓存

    分析：
    1. 需要在O(1)时间内插入和删除数据
    2. 需要对缓存内数据按照时间排序
    3.
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = DoubleList()
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1

        self.makeRecently(key)
        return self.map[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            # 改变value
            self.deleteKey(key)
            self.addRecently(key, value)
            return

        # 如果已达到最大cap 删除头结点
        if self.cache.getSize() == self.cap:
            self.removeLeastRecently()

        self.addRecently(key, value)
        return

    def makeRecently(self, k):
        node = self.map[k]
        self.cache.remove(node)
        self.cache.addLast(node)

    def deleteKey(self, key):
        node = self.map[key]
        self.cache.remove(node)
        del self.map[key]

    def addRecently(self, key, value):
        node = Node(key, value)
        self.cache.addLast(node)
        self.map[key] = value

    def removeLeastRecently(self):
        node = self.cache.removeFirst()
        del self.map[node.key]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.size = 0


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None
        self.size = 0

    def getSize(self):
        return self.size

    def addLast(self, x):
        """
        尾插
        :type x Node
        :return:
        """
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        x.prev = None
        x.next = None
        self.size -= 1
        return x

    def removeFirst(self):
        """
        头remove
        :return: Node
        """
        if self.head.next == self.tail:
            return None
        return self.remove(self.head.next)
