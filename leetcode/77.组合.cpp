/*
 * @lc app=leetcode.cn id=77 lang=cpp
 *
 * [77] 组合
 */

// @lc code=start

#include <vector>
using namespace std;

class Solution {
  void backtracking(int n, size_t k, long start, vector<int> &path, vector<vector<int>> &res) {
    if (path.size() == k) {
      res.push_back(path);
      return;
    }
    for (int i = start; i <= n; i++) {
      path.push_back(i);
      backtracking(n, k, i + 1, path, res);
      path.pop_back();
    }
  };

public:
  vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> res;
    vector<int> path;
    backtracking(n, k, 1, path, res);
    return res;
  }
};
// @lc code=end
