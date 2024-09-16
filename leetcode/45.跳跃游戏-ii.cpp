/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-15 20:17:23
 * @LastEditTime: 2024-09-16 15:07:46
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=45 lang=cpp
 *
 * [45] 跳跃游戏 II
 */
#include <vector>
// #include <yuri/yuri_log.hpp>


using namespace std;

// @lc code=start
class Solution {
public:
  int jump(const vector<int> &nums) {
    int size = nums.size(), step = 0, maxStep = 0, end = 0;
    for (int i = 0; i < size - 1; ++i) {
      maxStep = max(maxStep, i + nums[i]);
      if (i == end) {
        end = maxStep;
        ++step;
      }
    }
    return step;
  }
};


// int main() {
//   Solution s;
//   yinfo << s.jump({1,1,1,2,1});
//   return 0;
// }
// @lc code=end
