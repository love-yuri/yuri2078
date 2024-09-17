/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-17 17:50:18
 * @LastEditTime: 2024-09-17 19:48:32
 * @Description:
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 */

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
  string cover(string s) {
    string hash(26, 0);
    for (auto c : s) {
      hash[c - 'a']++;
    }
    return std::string(hash);
  }
  
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    vector<vector<string>> res;

    unordered_map<string, vector<string>> hash;
    for (auto s : strs) {
      hash[cover(s)].emplace_back(s);
      cout << cover(s) << endl;
    }

    for (auto &item : hash) {
      res.emplace_back(item.second);
    }
    return res;
  }
};
// @lc code=end
