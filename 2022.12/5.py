def palindrome(s: str, i: int, j: int) -> str:
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1:j]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i + 1)
            tmp = s1 if len(s1) > len(s2) else s2
            res = tmp if len(tmp) > len(res) else res
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.longestPalindrome("babadaasf4jdkogpaj")
    print(res)
