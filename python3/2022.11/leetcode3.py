class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        windows = {}
        n = len(s)
        # 初始化[left, right)窗口 左闭右开区间。
        # 设置左闭右开区间可以方便我们初始化两个指针都为0，此时[0, 0)窗口中没有任何元素，right右移一位后窗口中有一个元素
        # 如果设置左闭右闭区间[0,0]初始化时，窗口中已有一个元素。
        # 如果设置左开右开区间(0,0)初始化时，窗口中没有元素，right右移一位，窗口中还是没有元素。
        left, right = 0, 0
        result = 0
        while right < n:
            # 右侧指针移动 并构建map
            d = s[right]
            right += 1
            if d not in windows:
                windows[d] = 1
            else:
                windows[d] += 1
            print("[{},{})".format(left, right))
            # 判断左侧是否需要收缩
            while windows[d] > 1:
                c = s[left]
                windows[c] -= 1
                left += 1
            result = max(result, right - left)
        return result
