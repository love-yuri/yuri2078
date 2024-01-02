/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */

#include <vector>
#include <iostream>

using std::vector;

// @lc code=start
class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>> &matrix) {
    vector<int> res;
    int up = 0;
    int down = matrix.size() - 1;
    int left = 0;
    int right = matrix.at(0).size() - 1;
    while (true) {
      /* 先复制第一行的数据 */
      for (int i = left; i <= right; i++) {
        res.push_back(matrix[up][i]);
      }
      /* 将行数 + 1 并判断有没有到底  */
      if (++up > down) {
        break;
      }

      /* 赋值右侧一列 */
      for (int i = up; i <= down; i++) {
        res.push_back(matrix[i][right]);
      }
      /* 将右边界 - 1 并判断有没有到左边  */
      if (--right < left) {
        break;
      }

      /* 复制底部的数据 */
      for (int i = right; i >= left; i--) {
        res.push_back(matrix[down][i]);
      }
      /* 将底边界 - 1 并判断有没有到顶部  */
      if (--down < up) {
        break;
      }

      /* 赋值左侧一列 */
      for (int i = down; i >= up; i--) {
        res.push_back(matrix[i][left]);
      }
      /* 将左边界 + 1 并判断有没有到右边  */
      if (++left > right) {
        break;
      }
    }
    return res;
  }
};
// @lc code=end
