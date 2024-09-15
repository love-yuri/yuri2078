/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 */

// @lc code=start

#include <vector>
using namespace std;

class Solution {
public:
  int majorityElement(vector<int> &nums) {
    int count = 0, target;
    for (int num : nums) {
      // 如果计数器为0,当前元素一定是最多的元素
      // 因为 size(target) > n / 2, 那么一定能遇到count = 0时，target为最多的元素
      if (count == 0) {
        target = num;
        count = 1;
      } else if (num == target) {
        // 当元素相同时直接累加计数器
        count++;
      } else {
        // 元素不同时直接减一
        // 为什么不怕Target是正确的，最后减少到0呢？
        // 因为 size(target) > n / 2, 那么target的个数一定比其他元素多，所以最后target一定会留下
        count--;
      }
    }
    return target;
  }
};
// @lc code=end
