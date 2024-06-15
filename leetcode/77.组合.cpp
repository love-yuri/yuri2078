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
    // 判断我们需要生成的子集是不是满足题目的需要
    if (path.size() == k) {
      res.push_back(path);
      return;
    }
    // 从start开始
    for (int i = start; i <= n; i++) {
      path.push_back(i); // 将他添加到路径中，开始下一次的遍历
      backtracking(n, k, i + 1, path, res);
      path.pop_back(); // 将被遍历完的的路径弹出
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
