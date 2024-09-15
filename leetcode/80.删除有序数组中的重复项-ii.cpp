/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-09-03 22:52:52
 * @LastEditTime: 2024-09-04 13:54:13
 * @Description:
 */
/*
 * @lc app=leetcode.cn id=80 lang=cpp
 *
 * [80] 删除有序数组中的重复项 II
 */

// @lc code=start

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
  int removeDuplicates(vector<int> &nums) {
    if (nums.size() < 3) return nums.size();
    unordered_map<int, int> mp;
    int start = 0, count = 0;

    for (int x : nums) {
      mp[x]++;
      if (mp[x] <= 2) {
        nums[start++] = x;
        count++;
      }
    }
    return count;
  }
};
// @lc code=end
