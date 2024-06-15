/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-15 20:31:21
 * @LastEditTime: 2024-06-15 21:43:21
 * @Description: 01背包dp求解-滚动数组
 */
#include <vector>
#include <yuri/yuri_log.hpp>

using std::vector;

class Solution {
  vector<int> weights = {2, 3, 1, 5, 3, 3, 4};
  vector<int> values = {3, 4, 1, 2, 1, 5, 3};

public:
  // 求解01背包问题，物品个数为k， 背包容量为m
  int combinationSum(int k, int m) {
    // 一维滚动dp，每层都表示当前物品容量为j，他能实现的最大价值
    // 但是确认第n个物品的数组，需要从 0 - (n - 1)开始
    // 确认dp数组是 dp[j] 表示当背包容量为j时，他能实现的最大价值
    vector<int> dp(m + 1);

    // 确认dp递归公式
    // dp[j] 有两种可能，一种是放入这个物品，另一种是不放入这个物品
    // 当能够放入，并且放入时: dp[j] = dp[j - weights[i]] + values[i]
    // 当不能放入时: dp[j] = dp[j]
    // dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    // 初始化dp数组
    // 初始化第一个物品的数据
    for (int j = 0; j <= m; j++) {
      dp[j] = weights[0] <= j ? values[0] : 0;
    }

    // 开始dp
    for (int i = 1; i < k; i++) {
      // 只有在能够放入该物品时才更新，所以从最大容量开始更新
      for (int j = m; j >= weights[i]; j--) {
        // 依次更新数据
        dp[j] = std::max(dp[j], dp[j - weights[i]] + values[i]);
      }
    }

    yinfo << dp;

    // 返回他的最大价值
    return dp[m];
  }
};

int main() {
  Solution s;
  yinfo << "最大价值: " << s.combinationSum(7, 5);
  return 0;
}