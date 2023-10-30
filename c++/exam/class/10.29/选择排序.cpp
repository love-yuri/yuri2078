/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-10-29 16:51:34
 * @LastEditTime: 2023-10-29 16:54:41
 * @Description: 选择排序
 */
#include <iostream>
#include <vector>

void chooseSort(std::vector<int> &data) {
  int n = data.size();
  for (int i = 0; i < n - 1; i++) {
    int max_val = i;
    for (int j = i + 1; j < n; j++) {
      if (data[max_val] > data[j]) {
        max_val = j;
      }
    }
    int temp = data[i];
    data[i] = data[max_val];
    data[max_val] = temp;
  }
}

int main() {
  int n = 6;
  std::vector<int> num(n);
  for (int i = 0; i < n; i++) {
    std::cin >> num[i];
  }
  chooseSort(num);
  for (int n : num) {
    std::cout << n << " ";
  }
  std::endl(std::cout);
  return 0;
}