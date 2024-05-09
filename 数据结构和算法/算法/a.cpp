/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-05-07 14:03:18
 * @LastEditTime: 2024-05-07 14:06:43
 * @Description: 
 */
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int n, m;
  std::cin >> n;
  std::vector<int> vec(n);
  for (int i = 0; i < n; i++) {
    std::cin >> vec[i];
  }

  std::cin >> m;
  std::vector<int> search(m);
  for (int i = 0; i < m; i++) {
    std::cin >> search[i];
    auto val = std::find(vec.begin(), vec.end(), search[i]);
    if (val != vec.end()) {
      std::cout << "YES\n";
    } else {
      std::cout << "NO\n";
    }
  }
  return 0;
}