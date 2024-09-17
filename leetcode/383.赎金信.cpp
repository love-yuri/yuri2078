/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-17 14:39:18
 * @LastEditTime: 2024-09-17 14:42:03
 * @Description:
 * @lc app=leetcode.cn id=383 lang=cpp
 *
 * [383] 赎金信
 */
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
  bool canConstruct(string ransomNote, string magazine) {
    int cnt[26]{0};
    for (auto &c : magazine) {
      cnt[c - 'a']++;
    }
    for (auto &c : ransomNote) {
      if (cnt[c - 'a'] == 0) {
        return false;
      }
      cnt[c - 'a']--;
    }
    return true;
  }
};
// @lc code=end
