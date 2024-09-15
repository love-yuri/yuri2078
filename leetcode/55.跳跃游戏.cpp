/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 18:46:22
 * @LastEditTime: 2024-09-15 19:39:40
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=55 lang=cpp
 *
 * [55] 跳跃游戏
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
  bool canJump(vector<int> &nums) {
    // dp[i]表示从起点到i时剩余的步数
    vector<int> dp(nums.size(), 0);
    dp[0] = nums[0];
    for (int i = 1; i < nums.size(); i++) {
      // 如果到不了前一个点，则直接返回false
      if (dp[i - 1] < 1) {
        return false;
      }
      
      // 到达i点剩余数量 max(到前一个点剩余数量 - 1, 当前点能跳到的数量)
      dp[i] = max(dp[i - 1] - 1, nums[i]);
    }
    return dp[nums.size() - 1] >= 0;
  }
};
// @lc code=end
