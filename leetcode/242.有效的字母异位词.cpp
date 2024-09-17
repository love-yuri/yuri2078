/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-17 17:44:30
 * @LastEditTime: 2024-09-17 17:47:36
 * @Description:
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 */
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s.size() != t.size()) {
      return false;
    }
    int hash[26] = {0};
    for (auto c : s) {
      hash[c - 'a']++;
    }
    for (auto c : t) {
      hash[c - 'a']--;
    }
    for (auto i : hash) {
      if (i != 0) {
        return false;
      }
    }
    return true;
  }
};
// @lc code=end
