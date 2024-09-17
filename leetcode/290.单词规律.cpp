/*
 * @lc app=leetcode.cn id=290 lang=cpp
 *
 * [290] 单词规律
 */
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
  vector<string> split(string &s) {
    vector<string> res;
    string tmp;
    for (int i = 0; i < s.size(); ++i) {
      char &c = s[i];
      if (i == s.size() - 1) {
        tmp.push_back(c);
        res.push_back(tmp);
        return res;
      }

      if (c == ' ') {
        res.push_back(tmp);
        tmp.clear();
      } else {
        tmp.push_back(c);
      }
    }

    return res;
  }
  bool wordPattern(string pattern, string s) {
    auto words = split(s);

    if (pattern.size() != words.size()) {
      return false;
    }

    unordered_map<string, char> map;
    unordered_map<char, bool> pattern_map;
    for (int i = 0; i < pattern.size(); ++i) {
      auto &word = words[i];
      if (map.find(word) == map.end() && pattern_map.find(pattern[i]) == pattern_map.end()) {
        map[word] = pattern[i];
        pattern_map[pattern[i]] = true;
      }

      if (map[word] != pattern[i]) {
        return false;
      }
    }
    return true;
  }
};
// @lc code=end
