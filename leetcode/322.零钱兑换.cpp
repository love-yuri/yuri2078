/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 13:44:33
 * @LastEditTime: 2024-09-15 14:44:40
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
 */

#include <algorithm>
#include <vector>

using namespace std;

/**
本题使用动态规划求解
假如有 coins = [1, 2, 5], amount = 11
如果我们想求 amount = n 的最少硬币，我们只用求 amount = x (x 属于 amount - coins[i])
的最少硬币，然后加一即可为什么呢?
加入我们想要求 amount = 6的硬币，我们只用遍历 coins 中的每一个元素
然后求 amount = 6 - coins[i] 的最少硬币，然后加一即可
*/

// @lc code=start
class Solution {
public:
  int coinChange(vector<int> &coins, int amount) {

    if (amount == 0) return 0;
    if (amount < 0) return -1;

    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; ++i) {
      for (int j : coins) {
        if (i - j < 0) continue;
        dp[i] = min(dp[i], dp[i - j] + 1);
      }
    }
    return dp[amount] == amount + 1 ? -1 : dp[amount];
  }
};
// @lc code=end
