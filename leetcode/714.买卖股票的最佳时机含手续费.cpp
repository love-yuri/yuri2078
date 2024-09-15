/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 17:22:21
 * @LastEditTime: 2024-09-15 17:23:43
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=714 lang=cpp
 *
 * [714] 买卖股票的最佳时机含手续费
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
  int maxProfit(vector<int> &prices, int fee) {
        // dp 数组
    // dp[i][0] 表示第i天时 我没有持有股票的最大利润 此时我可能处于没有买入任何股票 也 可能是卖出了今天的股票
    // dp[i][1] 表示第i天时 我持有股票时的最大利润 此时我可能处于今天买入的股票 也可能是之前买入的股票
    vector<vector<int>> dp(prices.size(), vector<int>(2, 0));
    dp[0][0] = 0; // 第1天我没有持有股票的最大利润为0，因为我还没有买入任何股票
    dp[0][1] = -prices[0] - fee; // 第1天我持有股票的最大利润为 -prices[0]，因为我买入了一支股票

    for (int i = 1; i < prices.size(); i++) {
      // 第i天时 我没有持有股票的最大利润 = 前一天没买股票的最大利润 || 前一天买了股票今天卖出的利润
      dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);

      // 第i天时 我持有股票的最大利润 = 前一天买股票的最大利润 || 前一天卖了股票的最大利润 - 今天股票的价格
      dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee);
    }
    return dp[prices.size() - 1][0];
  }
};
// @lc code=end
