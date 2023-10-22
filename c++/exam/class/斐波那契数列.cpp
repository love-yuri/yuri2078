/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-10-13 08:02:10
 * @LastEditTime: 2023-10-13 08:31:16
 * @Description: 斐波那契数列
 */

#include <cmath>
#include <iostream>
#include <vector>

// int fb(int k) {
//   if (k < 3) {
//     return k != 0;
//   }
//   return fb(k - 1) + fb(k - 2);
// }

// int fb(int k) {
//   if (k < 3) {
//     return k != 0;
//   }
//   std::vector<int> db(k + 1);
//   db[0] = 0;
//   db[1] = 1;
//   for (int i = 2; i <= k; i++) {
//     db[i] = db[i - 1] + db[i - 2];
//   }
//   return db[k];
// }

int fb(int k) {
  const double sq_5 = std::sqrt(5);
  auto po_k = [](double x, double k) -> double {
    return std::pow(x, k);
  };
  return 1 / sq_5 * (po_k((1 + sq_5) / 2, k) - po_k((1 - sq_5) / 2, k));
}

int main() {
  int k = 0;
  std::cin >> k;
  std::cout << fb(k);
  std::endl(std::cout);
  return 0;
}
