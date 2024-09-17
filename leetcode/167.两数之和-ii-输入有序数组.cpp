/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-17 14:15:51
 * @LastEditTime: 2024-09-17 14:20:25
 * @Description:
 * @lc app=leetcode.cn id=167 lang=cpp
 *
 * [167] 两数之和 II - 输入有序数组
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    int left = 0, right = numbers.size() - 1;
    while (left < right) {
      if (numbers[left] + numbers[right] == target) {
        return {left + 1, right + 1};
      } else {
        if (numbers[left] + numbers[right] < target) {
          left++;
        } else {
          right--;
        }
      }
    }
    return {};
  }
};
// @lc code=end
