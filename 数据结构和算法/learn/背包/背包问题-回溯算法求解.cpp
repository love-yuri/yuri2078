/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-15 18:07:07
 * @LastEditTime: 2024-06-15 21:07:13
 * @Description: 回溯算法解决背包问题
 */
#include <vector>
#include <yuri/yuri_log.hpp>

using std::vector;

class Solution {
  vector<int> weights = {2, 3, 1, 5, 3, 3, 4};
  vector<int> values = {3, 4, 1, 2, 1, 5, 3};
  vector<int> res;
  int max_value = 0;
  vector<int> path;

  void backtracking(unsigned k, int value, int left, int start) {
    if (path.size() > k || left < 0) {
      return;
    }
    if (value > max_value) {
      max_value = value;
      res = path;
    }
    for (unsigned i = start; i < weights.size(); i++) {
      path.push_back(values[i]);
      backtracking(k, value + values[i], left - weights[i], i + 1);
      path.pop_back();
    }
  }

public:
  // 求解01背包问题，最多能拿的物品个数为k， 背包容量为m
  int combinationSum(int k, int m) {
    // values = vector<int>(k);
    // weights = vector<int>(k);
    // for (int i = 0; i < k; i++) {
    //   std::cin >> weights[i];
    // }
    // for (int i = 0; i < k; i++) {
    //   std::cin >> values[i];
    // }

    backtracking(k, 0, m, 0);
    // std::cout << max_value;
    yinfo << "sum -> " << max_value << "\n"
      << res;
    return 1;
  }
};

int main() {
  // int m, n;
  // std::cin >> m >> n;
  Solution s;
  s.combinationSum(7, 5);
  return 0;
}