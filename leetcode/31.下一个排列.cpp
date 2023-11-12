/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-10-12 08:38:51
 * @LastEditTime: 2023-11-01 21:18:48
 * @Description: [31] 下一个排列
 */

// @lc code=start

#include <vector>

using namespace std;

class Solution {
public:
  void nextPermutation(vector<int> &nums) {
    const int size = nums.size();
    for (int i = size - 1; i > 0; i--) {
      if (nums[i] > nums[i - 1]) {
        int t = nums[i];
        nums[i] = nums[i - 1];
        nums[i - 1] = t;
        return;
      }
    }

    int l = 0, r = size - 1;
    while (l < r) {
      int t = nums[r];
      nums[r] = nums[l];
      nums[l] = t;
      l++;
      r--;
    }
  }
};
// @lc code=end
