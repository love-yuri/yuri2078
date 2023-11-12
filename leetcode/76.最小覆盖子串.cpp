/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2023-11-01 22:46:58
 * @Description: 最小覆盖字串
 */
/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
#include <cstdint>
#include <string>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
  string minWindow(string s, string t) {
    unordered_map<char, int> need, window;
    string ret;
    int maxlan = INT32_MAX;
    for (char c : t) {
      need[c]++;
    }
    int left = 0, right = 0, start = 0, valid = 0;
    while (right < s.size()) {
      char c = s[right];
      right++;
      if (need.count(c)) {
        window[c]++;
        if (window[c] == need[c]) {
          valid++;
        }
      }
      while (valid == need.size()) {
        if (right - left < maxlan) {
          maxlan = right - left;
          start = left;
        }
        char out = s[left++];
        if (need.count(out)) {
          if(window[out] == need[out]) {
            valid--;
          }
          window[out]--;
        }
      }
    }
    return maxlan == INT32_MAX ? "" : s.substr(start, maxlan);
  }
};
// int main() {
//   Solution so;
//   cout << so.minWindow("ab", "b") << endl;
//   return 0;
// }
// @lc code=end
