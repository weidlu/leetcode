from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            counter[char] += 1
            while counter[char] > 1:
                counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


if __name__ == '__main__':
    # Example usage:
    s = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)  # Expected output: 3 (the substring is "abc")
