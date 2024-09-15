/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 17:05:51
 * @LastEditTime: 2024-09-15 17:21:35
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=123 lang=cpp
 *
 * [123] 买卖股票的最佳时机 III
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int size = prices.size(), k = 2;
    // dp[i][j][0] 表示第i天，最多交易j + 1次，手上没有股票的最大利润
    // dp[i][j][1] 表示第i天，最多交易j + 1次，手上有股票的最大利润
    vector<vector<vector<int>>> dp = vector<vector<vector<int>>>(size, vector<vector<int>>(k + 1, vector<int>(2, 0)));

    // 初始化dp数组
    // 第一天，无论要交易多少次，结果是不变的
    for (int i = 1; i <= k; ++i) {
      dp[0][i][0] = 0;          // 第一天，最多交易1次， 手上没有股票的最大利润为0，因为没有买入
      dp[0][i][1] = -prices[0]; // 第一天，最多交易1次，手上有股票的最大利润为 -prices[0]，因为买入股票了
    }

    // 第 i + 1天数据
    for (int i = 1; i < size; i++) {
      for (int j = 1; j <= k; j++) {
        // 第i天，最多交易j次，手上没有股票的最大利润 =
        // max(今天卖出股票的最大利润， 今天不买也不卖股票的最大利润)
        // 今天卖出股票的最大利润 = i - 1天，最多交易j次，手上有股票的最大利润 + 今天股票价格
        // 今天不买也不卖股票的最大利润 = i - 1天，最多交易j次，手上没有股票的最大利润
        dp[i][j][0] = max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][0]);

        // 第i天，最多交易j次，手上有股票的最大利润 =
        // max(今天不买股票的最大利润，今天买股票的最大利润)
        // 今天不买: i - 1天，最多交易j次，手上有股票的最大利润
        // 今天买: i - 1天，最多交易j - 1次，手上没有股票的最大利润 - 今天股票价格

        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]);
      }
    }

    return dp[size - 1][k][0];
  }
};
// @lc code=end
