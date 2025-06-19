class Solution:
    def climbStairs(self, n: int) -> int:
        #         l(i) = l(i-1) + l(i-2)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    # Example usage:
    n = 5
    solution = Solution()
    result = solution.climbStairs(n)
    print(result)  # Expected output: 8 (the number of distinct ways to climb 5 stairs)
