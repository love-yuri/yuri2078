/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-16 21:17:49
 * @LastEditTime: 2024-09-16 21:20:22
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */
#include <cctype>
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
  bool isPalindrome(string s) {
    int start = 0;
    for (char c : s) {
      if (isalpha(c) || isdigit(c)) {
        s[start++] = tolower(c);
      }
    }
    s.resize(start);
    int l = 0, r = s.size() - 1;
    while (l < r && s[l] == s[r]) {
      l++;
      r--;
    }
    return l >= r;
  }
};
// @lc code=end
