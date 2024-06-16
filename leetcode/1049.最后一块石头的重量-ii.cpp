/*
 * @lc app=leetcode.cn id=1049 lang=cpp
 *
 * [1049] 最后一块石头的重量 II
 */

#include <algorithm>
#include <numeric>
#include <vector>
// #include <yuri/yuri_log.hpp>

using std::vector;

// @lc code=start
class Solution {
public:
  // 将题目转化成01背包问题
  // 他需要粉碎后的差值最小，那么就是尽可能是将两边分成相等的两份
  // 那么最优情况就是能分成两个合相等的子集-就是416分割字串的题目
  int lastStoneWeightII(vector<int> &stones) {
    int sum = std::accumulate(stones.begin(), stones.end(), 0);
    int mid = sum / 2;
    vector<int> dp = vector<int>(mid + 1, 0);
    for (unsigned i = 0; i < stones.size(); i++) {
      for (unsigned j = mid; j >= unsigned(stones[i]); j--) {
        dp[j] = std::max(dp[j], dp[j - stones[i]] + stones[i]);
      }
    }

    // dp求解完成后 dp[mid] 就是能凑出的最接近中间值的价值了
    // 也就是左侧最多凑错 dp[mid]的价值，那么右侧就剩余 sum - dp[mid]的价值
    // 他们最后的差值就是 (sum - dp[mid]) - dp[mid] 右侧减去左侧
    return (sum - dp[mid]) - dp[mid];
  }
};

// int main() {
//   vector<int> v = {31, 26, 33, 21, 40};
//   yinfo << Solution().lastStoneWeightII(v);
//   return 0;
// }
// @lc code=end
