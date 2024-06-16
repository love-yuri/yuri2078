/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-15 21:45:04
 * @LastEditTime: 2024-06-15 22:47:31
 * @Description:
 */

#include <iostream>
#include <functional>
#include <vector>

using std::vector;

template <typename U, typename F>
vector<int> &operator|(U &&v, F f) {
  for (auto &x : v) {
    f(x);
  }
  return v;
}

int main() {
  std::vector v{1, 2, 3};
  std::function f{[](const int &i) { std::cout << i << ' '; }};
  auto f2 = [](int &i) { i *= i; };
  v | f2 | f;
}