/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
#include <vector>
#include <iostream>

using namespace std;

/* 思路 模拟队列 */
class Solution {
public:
  vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> res(n, vector<int>(n, 0));
    int num = 1;
    for (int i = 0; i < n / 2; i++) {
      for (int k = 0; k < n - 1 - i * 2; k++) {
        res[i][i + k] = num++;
      }
      for (int k = 0; k < n - 1 - i * 2; k++) {
        res[i + k][n - i - 1] = num++;
      }
      for (int k = 0; k < n - 1 - i * 2; k++) {
        res[n - i - 1][n - i - k - 1] = num++;
      }
      for (int k = 0; k < n - 1 - i * 2; k++) {
        res[n - i - 1 - k][i] = num++;
      }
    }
    if (n % 2) {
      res[n / 2][n / 2] = num;
    }
    return res;
  }
};
// @lc code=end
