#include <iostream>

void search(std::string &s, std::string &t) {
  int count = 0;
  for (size_t i = 0; i < s.size() - t.size() + 1; i++) {
    int k = i;
    for (size_t j = 0; j < t.size(); j++) {
      count++;
      if (t.at(j) != s.at(k)) {
        break;
      }
      k++;
    }
    if (k - i == t.size()) {
      std::cout << i << " " << count;
      return;
    }
  }
  std::cout << -1 << " " << count;
}
int main() {
  std::string s, t;
  std::cin >> s;
  std::cin >> t;
  search(s, t);
  std::endl(std::cout);
  return 0;
}