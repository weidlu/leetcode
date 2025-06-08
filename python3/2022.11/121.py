class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return dp[n - 1][0]


if __name__ == "__main__":
    _prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(_prices))
