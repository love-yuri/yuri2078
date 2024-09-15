/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-05 20:42:55
 * @LastEditTime: 2024-09-15 17:23:06
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=122 lang=cpp
 *
 * [122] 买卖股票的最佳时机 II
 */

// @lc code=start
#include <vector>
using namespace std;

// 3维dp版本
// 因为需要考虑最多交易几次，所以需要多一维
// 但是本题不需要考虑交易次数，所以可以简化为2维dp
// 我们不关心交易了多少次，那么今天如果没有股票，最大利润就是
// max(n - 1天没有持有股票的利润, n - 1天持有股票的利润 + 今天卖出的利润)

// 如果今天持有股票，那么最大利润就是(不用考虑交易次数， 所以计算今天买入利润不是-prices[i], 而是之前n - 1天的最大利润)
// max(n - 1天持有股票的利润, n - 1天没有持有股票的利润 - 今天买入的利润)
class Solution2 {
public:
  int maxProfit(vector<int> &prices) {
    int size = prices.size();
    // dp[i][j][0] 表示第i天，最多交易j + 1次，手上没有股票的最大利润
    // dp[i][j][1] 表示第i天，最多交易j + 1次，手上有股票的最大利润
    vector<vector<vector<int>>> dp = vector<vector<vector<int>>>(size, vector<vector<int>>(size, vector<int>(2, 0)));

    // 初始化dp数组
    // 第一天，无论要交易多少次，结果是不变的
    for (int i = 0; i < size; ++i) {
      dp[0][i][0] = 0;          // 第一天，最多交易1次， 手上没有股票的最大利润为0，因为没有买入
      dp[0][i][1] = -prices[0]; // 第一天，最多交易1次，手上有股票的最大利润为 -prices[0]，因为买入股票了
    }

    // 第 i + 1天数据
    for (int i = 1; i < size; ++i) {
      dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][0][1] + prices[i]);
      dp[i][0][1] = max(dp[i - 1][0][1], -prices[i]);
      for (int j = 1; j < size; j++) {
        // 第i天，最多交易j + 1次，手上没有股票的最大利润 =
        // max(今天交易最大利润， 今天不交易最大利润)
        // 今天交易最大利润 = i - 1天，最多交易j次，手上有股票的最大利润 + 今天股票价格
        // 今天不交易最大利润 = i - 1天，最多交易j + 1次，手上没有股票的最大利润
        dp[i][j][0] = max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][0]);

        // 第i天，最多交易j + 1次，手上有股票的最大利润 =
        // max(今天不交易最大利润， 过去i - 1天最多交易j次，手上没有股票的最大利润 + 买入今天股票价格)
        // 今天不交易最大利润 = i - 1天，最多交易j + 1次，手上有股票的最大利润

        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]);
      }
    }

    return dp[size - 1][size - 1][0];
  }
};
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    // dp 数组
    // dp[i][0] 表示第i天时 我没有持有股票的最大利润 此时我可能处于没有买入任何股票 也 可能是卖出了今天的股票
    // dp[i][1] 表示第i天时 我持有股票时的最大利润 此时我可能处于今天买入的股票 也可能是之前买入的股票
    vector<vector<int>> dp(prices.size(), vector<int>(2, 0));
    dp[0][0] = 0; // 第1天我没有持有股票的最大利润为0，因为我还没有买入任何股票
    dp[0][1] = -prices[0]; // 第1天我持有股票的最大利润为 -prices[0]，因为我买入了一支股票

    for (int i = 1; i < prices.size(); i++) {
      // 第i天时 我没有持有股票的最大利润 = 前一天没买股票的最大利润 || 前一天买了股票今天卖出的利润
      dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);

      // 第i天时 我持有股票的最大利润 = 前一天买股票的最大利润 || 前一天卖了股票的最大利润 - 今天股票的价格
      dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
    }
    return dp[prices.size() - 1][0];
  }
};
// @lc code=end
