/*
 * @lc app=leetcode.cn id=189 lang=cpp
 *
 * [189] 轮转数组
 */

// @lc code=start
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
  void resolve(vector<int> &nums, int start, int end) {
    while (start < end) {
      swap(nums[start], nums[end]);
      start++;
      end--;
    }
  }
  void rotate(vector<int> &nums, int k) {
    int size = nums.size();
    if (k % size == 0) {
      return;
    }
    k = k % size;
    // 先反转整个数组
    resolve(nums, 0, size - 1);
    // 再反转前k个元素
    resolve(nums, 0, k - 1);
    // 再反转剩下的元素
    resolve(nums, k, size - 1);
  }
};
// @lc code=end
