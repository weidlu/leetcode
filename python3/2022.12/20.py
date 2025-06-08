class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {'(': ')', '{': '}', '[': ']'}
        for _s in list(s):
            if len(stack) > 0 and bracketMap[stack[-1]] == _s:
                stack.pop()
            elif _s not in bracketMap:
                return False
            else:
                stack.append(_s)
        return len(stack) == 0


if __name__ == "__main__":
    input = "(){[]}"
    s = Solution()
    print(s.isValid(input))
