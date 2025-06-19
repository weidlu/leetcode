class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, char in enumerate(s):
            if stack:
                top = stack[-1]
                if top == "(" and char == ")" or top == "[" and char == "]" or top == "{" and char == "}":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    # Example usage:
    s = "({[)"
    solution = Solution()
    result = solution.isValid(s)
    print(result)  # Expected output: True
