/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-15 20:31:21
 * @LastEditTime: 2024-06-15 21:13:47
 * @Description: 01背包dp求解
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
    // 确认dp数组是 dp[i][j] 表示前i个物品，背包容量为j时，能够获得的最大价值
    vector<vector<int>> dp(k, vector<int>(m + 1));

    // dp[i][j] 有两种可能，一种是放入第i个物品，另一种是不放入第i个物品
    // 如果放入第i件物品，那么剩余容量就是 j - weights[i]，那么此时还能从 i - 1个物品中，放入weights[j - weights[i]]容量的物品，总容量就是dp[i - 1][j - weight[i]] + value[i]
    // 如果是不放入第i件物品，那么dp[i][j] = dp[i - 1][j]
    // 最终确认递归公式为 max(放入第i件物品，不放入第i件物品)
    // 确认递归公式: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i]);


    // 初始化dp数组
    // 由递归公式知道，我们需要dp[i - 1]的所有数据，所以初始化dp[0] 就ok了
    for (int j = 0; j <= m; j++) {
      dp[0][j] = weights[0] <= j ? values[0] : 0;
    }

    // 开始dp
    for (int i = 1; i < k; i++) {
      for (int j = 0; j <= m; j++) {
        // 只有当j大于第i个物品的重量时，才放入第i个物品
        if (weights[i] <= j) {
          dp[i][j] = std::max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i]);
        } else {
          // 否则只能不放入第i个物品
          dp[i][j] = dp[i - 1][j];
        }
      }
    }

    yinfo << dp;

    // 返回他的最大价值
    return dp[k - 1][m];
  }
};

int main() {
  Solution s;
  yinfo << "最大价值: " << s.combinationSum(7, 5);
  return 0;
}