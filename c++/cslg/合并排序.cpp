#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

void merge(vector<int> &nums, int left, int mid, int right) {
  vector<int> temp(right - left + 1);
  int i = left;
  int j = mid + 1;
  int k = 0;
  while (i <= mid && j <= right) {
    temp[k++] = nums[i] < nums[j]? nums[i++] : nums[j++];
  }
  while (i <= mid) {
    temp[k++] = nums[i++];
  }
  while (j <= right) {
    temp[k++] = nums[j++];
  }
  for (int i = 0; i < temp.size(); i++) {
    nums[left + i] = temp[i];
  }
}

void mergeSort(vector<int> &num, int begin, int end) {
  if (begin >= end) {
    return;
  }
  int mid = (begin + end) >> 1;
  mergeSort(num, begin, mid);
  mergeSort(num, mid + 1, end);
  merge(num, begin, mid, end);
}

int main() {
  vector<int> num(6);
  for (int i = 0; i < num.size(); i++) {
    std::cin >> num[i];
  }
  mergeSort(num, 0, num.size() - 1);
  for (int i = 0; i < num.size(); i++) {
    std::cout << num[i] << " ";
  }
  std::endl(std::cout);
  return 0;
}