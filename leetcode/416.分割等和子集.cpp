/*
 * @lc app=leetcode.cn id=416 lang=cpp
 *
 * [416] 分割等和子集
 */

// @lc code=start

#include <numeric>
#include <vector>

// #include <yuri/yuri_log.hpp>

using std::vector;

class Solution {
public:
  // 将问题分解成01 背包问题。
  // 他需要将元素分割成合相等的两个子集
  // 每个子集的和都是总和的一半
  // 那么我们只要找到 一个集合他的总和 等于 总和的一半即可
  // 因为他占总和的一半，那么剩下的必然也是一半
  // 直接变成01背包问题
  bool canPartition(vector<int> &nums) {
    int mid = std::accumulate(nums.begin(), nums.end(), 0);
    // 如果总和是奇数，则无法分割成两个子集
    if (mid % 2 == 1) {
      return false;
    }
    mid = mid / 2;
    // 动态规划
    vector<int> dp(mid + 1, 0);

    for (unsigned i = 0; i < nums.size(); i++) {
      for (unsigned j = mid; j >= unsigned(nums[i]); j--) {
        dp[j] = std::max(dp[j], dp[j - nums[i]] + nums[i]);
      }
    }
    
    return dp[mid] == mid;
  }
};

// int main() {
//   vector<int> vec = {1, 5, 11, 5};
//   Solution s;
//   yinfo << std::boolalpha << s.canPartition(vec);
//   return 0;
// }
// @lc code=end
