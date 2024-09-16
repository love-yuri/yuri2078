/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-16 20:43:57
 * @LastEditTime: 2024-09-16 21:07:07
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=380 lang=cpp
 *
 * [380] O(1) 时间插入、删除和获取随机元素
 */
#include <cstdlib>
#include <utility>
#include <vector>
#include <unordered_map>
using namespace std;

// @lc code=start
class RandomizedSet {
  unordered_map<int, int> map;
  vector<int> vec;

public:
  RandomizedSet() {
  }

  bool insert(int val) {
    if (map.find(val) != map.end()) {
      return false;
    }
    vec.push_back(val);
    map[val] = vec.size() - 1;
    return true;
  }

  bool remove(int val) {
    if (map.find(val) == map.end()) {
      return false;
    }
    int idx = map[val];
    swap(vec[vec.size() - 1], vec[idx]);
    vec.pop_back();
    map[vec[idx]] = idx;
    map.erase(val);
    return true;
  }

  int getRandom() {
    return vec[rand() % vec.size()];
  }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
// @lc code=end
