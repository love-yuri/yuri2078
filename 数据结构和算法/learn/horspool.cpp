#include <iostream>
#include <string>
#include <vector>

int horspool(std::string &s, std::string &t, int &count) {
  int n = s.size();
  int m = t.size();

  if (m > n) {
    return -1;
  }
  std::vector<int> bad_char(256, m);
  for (int i = 0; i < m - 1; ++i) {
    bad_char[t[i]] = m - i - 1;
  }
  int skip;
  for (int i = 0; i <= n - m;) {
    skip = 0;
    for (int j = m - 1; j >= 0; --j) {
      count++;
      if (s[i + j] != t[j]) {
        skip = bad_char[s[i + j]];
        break;
      }
    }

    if (skip == 0) {
      return i;
    }
    i += skip;
  }

  return -1;
}

int main() {
  std::string s, t;
  int count = 0;

  std::cin >> s;
  std::cin >> t;

  std::cout << horspool(s, t, count) << " " <<  count;
  std::endl(std::cout);

  return 0;
}
