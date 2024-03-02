#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

int sort(vector<int> &num, int begin, int end) {
  int key = num[begin];
  int next = end;
  while (begin != end) {
    if (key > num[next]) {
      num[begin] = num[next];
      next = ++begin;
    } else {
      num[end] = num[next];
      next = --end;
    }
  }
  num[begin] = key;
  return begin;
}

void quickSort(vector<int> &num, int start, int end) {
  if (start < end) {
    int k = sort(num, start, end);
    quickSort(num, start, k - 1);
    quickSort(num, k + 1, end);
  }
}
int main() {
  vector<int> num(6);
  for (int i = 0; i < num.size(); i++) {
    std::cin >> num[i];
  }
  quickSort(num, 0, num.size() - 1);
  for (int i = 0; i < num.size(); i++) {
    std::cout << num[i] << " ";
  }
  std::endl(std::cout);
  return 0;
}