/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-10-29 16:51:34
 * @LastEditTime: 2023-10-29 16:55:26
 * @Description: 冒泡排序
 */
#include <iostream>
#include <vector>

void chooseSort(std::vector<int> &data) {
  int n = data.size();
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (data[j] > data[j + 1]) {
        int temp = data[j];
        data[j] = data[j + 1];
        data[j + 1] = temp;
      }
    }
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