/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 20:17:23
 * @LastEditTime: 2024-09-15 23:45:35
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=45 lang=cpp
 *
 * [45] 跳跃游戏 II
 */
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
  int jump(const vector<int> &nums) {
    // dp[i] 从0出发，到i点的最小步数
    int current = 1, step = nums[0], maxStep = 0, dp = 0;
    for (int i = 1; i < nums.size(); ++i) {
      // 从起点出发，如果起点的剩余步数 > 0, 则可以直接从起点到达i点
      // 此时所需步数 = 0点到达起点的步数 + 1
      if (step > 0) {
        dp = current;
        // 计算如果到达起点不能一次性到达某点时，从i点出发能前进的最大步数
        maxStep = max(maxStep, nums[i] - 1);
        step--;
      } else {
        // 起点步数用尽，要到达此点，步数 + 1
        dp = ++current;
        // 更新从i点出发能前进的最大步数
        step = maxStep;
        maxStep = 0;
      }
    }
    return dp;
  }
};

// #include <yuri/yuri_log.hpp>

// int main() {
//   Solution s;
//   yinfo << s.jump({1,1,1,2,1});
//   return 0;
// }
// @lc code=end
