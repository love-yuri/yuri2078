/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-16 19:52:21
 * @LastEditTime: 2024-09-16 20:27:17
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=274 lang=cpp
 *
 * [274] H 指数
 */
#include <algorithm>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
  int hIndex(vector<int> &citations) {
    // 1、排序
    sort(citations.begin(), citations.end());
    int res = 0;

    // 0 1 3 5 6
    for (int i = citations.size() - 1; i >= 0; i--) {
      if (citations[i] > res) {
        res++;
      } else {
        return res;
      }
    }
    return res;
  }
};
// @lc code=end
