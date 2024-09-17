/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-17 14:43:38
 * @LastEditTime: 2024-09-17 15:21:58
 * @Description:
 * @lc app=leetcode.cn id=205 lang=cpp
 *
 * [205] 同构字符串
 */
#include <string>

class Solution {
public:
  std::string &cover(std::string &s) {
    // 创建隐射表， 默认从1开始映射
    int cnt[256] = {0}, start = 1;
    for (int i = 0; i < s.size(); i++) {
      int pos = static_cast<int>(s[i]);

      // 如果隐射表中没有该字符，则添加映射关系
      if (cnt[pos] == 0) {
        cnt[pos] = start++;
      }

      // 将字符替换为映射值
      s[i] = cnt[pos];
    }
    return s;
  }

  bool isIsomorphic(std::string s, std::string t) {
    if (s.size() != t.size()) {
      return false;
    }
    return cover(s) == cover(t);
  }
};
// @lc code=end
