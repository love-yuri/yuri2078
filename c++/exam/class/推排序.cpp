/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-24 08:54:54
 * @LastEditTime: 2023-11-24 09:10:59
 * @Description: 堆排序
 */
#include <iostream>
#include <array>

void swap(int &x, int &y) {
  int k = x;
  x = y;
  y = k;
}

void heapAdjust(std::array<int, 6> &num, int v) {
  for (int parent = v / 2 - 1; parent >= 0; parent--) {
    while (parent * 2 + 1 < v) {
      int lchild = parent * 2 + 1;
      int rchild = parent * 2 + 2;
      int next = rchild;
      if (rchild >= v || num[lchild] > num[rchild]) {
        next = lchild;
      }
      if (num[parent] < num[next]) {
        swap(num[parent], num[next]);
      } else {
        break;
      }
    }
  }
  swap(num[v - 1], num[0]);
}

void heapSort(std::array<int, 6> &num) {
  for (int i = 0; i < num.size() - 1; i++) {
    heapAdjust(num, num.size() - i);
  }
}

int main() {
  std::array<int, 6> num;
  for (int i = 0; i < 6; i++) {
    std::cin >> num[i];
  }
  heapSort(num);
  for (int i = 0; i < 6; i++) {
    std::cout << num[i] << " ";
  }
  std::cout << "\n";
  return 0;
}
