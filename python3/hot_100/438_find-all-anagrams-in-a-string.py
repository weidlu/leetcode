from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        window_len = len(p)
        window_counter = Counter()
        p_counter = Counter(p)
        for right in range(len(s)):
            window_counter[s[right]] += 1

            if right - left + 1 == window_len:
                if window_counter == p_counter:
                    res.append(left)
                window_counter[s[left]] -= 1
                if window_counter[s[left]] == 0:
                    del window_counter[s[left]]
                left += 1
        return res


if __name__ == '__main__':
    # Example usage:
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    result = solution.findAnagrams(s, p)
    print(result)  # Expected output: [0, 6]
