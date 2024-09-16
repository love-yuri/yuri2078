/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-16 21:42:51
 * @LastEditTime: 2024-09-16 21:44:08
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] 判断子序列
 */
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
  bool isSubsequence(string s, string t) {
    int i = 0, j = 0;
    while (i < s.size() && j < t.size()) {
      if (s[i] == t[j]) {
        i++;
      }
      j++;
    }
    return i == s.size();
  }
};
// @lc code=end
