/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> res(n, vector<int>(n));
    int i = 0, j = 0;
    for (int num = 1; num <= n * n;) {
        cout << i << " " << j << " "  << num++ << "\n";
    //   res[i][j] = num++;
      for (int t = 0; t < 4; t++) {
        int &p = t % 2 ? i : j;
        for (int k = 0; k < n - 1; k++) {
          if (t == 3 && k == n - 2) {
            break;
          }
          t < 2 ? p++ : p--;
        //   res[i][j] = num++;
            cout << i << " " << j << " - " << num++ << "\n";
        }
      }
        cout << i << " " << ++j << " " << num++ << "\n";
    //   res[i][++j] = num++;
    }

    return {{}};
  }
};

int main() {
  Solution s;
  auto ret = s.generateMatrix(4);
  for (int i = 0; i < ret.size(); i++) {
    for (int j = 0; j < ret[i].size(); j++) {
      cout << ret[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
// @lc code=end
