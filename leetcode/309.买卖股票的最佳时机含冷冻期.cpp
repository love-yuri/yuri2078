/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 16:27:15
 * @LastEditTime: 2024-09-15 16:45:23
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=309 lang=cpp
 *
 * [309] 买卖股票的最佳时机含冷冻期
 */

// @lc code=start

#include <vector>
using namespace std;

class Solution {
public:
  int maxProfit(vector<int> &prices) {
    // dp 数组
    // dp[i][0] 表示第i天时 我没有持有股票的最大利润 此时我可能处于没有买入任何股票 也 可能是卖出了今天的股票
    // dp[i][1] 表示第i天时 我持有股票时的最大利润 此时我可能处于今天买入的股票 也可能是之前买入的股票
    vector<vector<int>> dp(prices.size(), vector<int>(2, 0));
    dp[0][0] = 0;          // 第1天我没有持有股票的最大利润为0，因为我还没有买入任何股票
    dp[0][1] = -prices[0]; // 第1天我持有股票的最大利润为 -prices[0]，因为我买入了一支股票

    if (prices.size() == 1) {
      return dp[0][0];
    }
    dp[1][0] = max(0, prices[1] - prices[0]); 
    dp[1][1] = max(-prices[0], -prices[1]); 

    for (int i = 2; i < prices.size(); i++) {
      // 第i天时 我没有持有股票的最大利润 =
      // max(今天卖出的利润 + i - 1天没卖股票的利润) 为什么这里不考虑冻结期呢? 取得是dp[i - 1][0]而不是dp[i - 2][0]呢?
      // 因为今天没卖股票，所以昨天一定是可以卖的。
      dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);

      // 第i天时 我持有股票的最大利润 = 前一天买股票的最大利润 || 前两天卖了股票的最大利润 - 今天股票的价格
      // 为什么是前两天？因为冷冻期是1天，所以如果今年能卖股票，那么昨天肯定没有卖出股票，所以
      // 利润是: max(昨天没有卖出股票的最大利润， 今天卖出的利润 + 前天卖出股票后的利润)
      dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i]);
    }
    return dp[prices.size() - 1][0];
  }
};
// @lc code=end
