# 贪心法：一次遍历，记录历史最低价和最大利润
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # 历史最低买入价
        max_profit = 0            # 历史最大利润
        for price in prices:
            # 遇到更低的买入价，更新
            if price < min_price:
                min_price = price
            # 否则按当前价卖出，计算利润并更新最大值
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

    def maxProfit_dp(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # dp_i_0：第 i 天不持有时的最大收益
        # dp_i_1：第 i 天持有时的最大收益
        dp_i_0, dp_i_1 = 0, -prices[0]
        for price in prices[1:]:
            # 不持有：要么延续前一天不持有，要么今天卖出（前一天持有 + 今天价格）
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            # 持有：要么延续前一天持有，要么今天买入（- 今天价格）
            dp_i_1 = max(dp_i_1, -price)
        # 最后肯定是不持有才能最大化收益
        return dp_i_0

if __name__ == "__main__":
    # Example usage:
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)  # Expected output: 5 (buy at 1 and sell at 6)

    # Using dynamic programming approach
    result_dp = solution.maxProfit_dp(prices)
    print(result_dp)  # Expected output: 5 (same logic as above)