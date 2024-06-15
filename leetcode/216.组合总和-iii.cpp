/*
 * @lc app=leetcode.cn id=216 lang=cpp
 *
 * [216] 组合总和 III
 */

#include <vector>
// #include <yuri/yuri_log.hpp>

using std::vector;

// @lc code=start
class Solution {
  vector<vector<int>> res;
  vector<int> path;

  // k 需要的元素个数
  // left 剩余需要添加的价值
  // 起点
  void backtracking(unsigned long k, int left, int start) {
    if (path.size() == k) {
      if (left == 0) {
        res.push_back(path);
      }
      return;
    }
    for (int i = start; i <= 9 && i <= left; i++) {
      path.push_back(i);
      backtracking(k, left - i, i + 1);
      path.pop_back();
    }
  }

public:
  vector<vector<int>> combinationSum3(int k, int n) {
    backtracking(k, n, 1);
    return res;
  }
};

// int main() {
//   Solution s;
//   auto b = s.combinationSum3(3, 9);
//   yinfo << b;
//   return 0;
// }
// @lc code=end
