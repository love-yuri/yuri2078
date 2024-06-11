#include <map>
#include <vector>
#include <yuri/yuri_log.hpp>
#include <yuri/yuri.h>

/**
 * A* search algorithm in C++
 * 通过a*算法在C++中找到结果
 */

// #include <iostream>
// #define yinfo std::cout

using std::vector;
using std::multimap;

void search(const int weight, const vector<int> &pos, vector<vector<int>> &map, multimap<int, vector<int>> &path) {
  // 获取当前坐标
  int x = pos[0];
  int y = pos[1];

  auto check = [&](int x, int y) {
    if (x < 0 || x >= int(map.size()) || y < 0 || y >= int(map[0].size()) || map[x][y] != 0 || (x == 2 && y == 1)) {
      return;
    }
    map[x][y] = weight + 1;
    path.insert({weight + 1, {x, y}});
  };

  check(x, y - 1); // 上
  check(x, y + 1); // 下
  check(x - 1, y); // 左
  check(x + 1, y); // 右
}

auto ASearch(vector<vector<int>> &vec) {
  int count = 0;
  // 待搜索的map， key是G， value是下表
  multimap<int, vector<int>> map = multimap<int, vector<int>>();
  // 存储最短路径
  std::map<vector<int>, vector<vector<int>>> path;

  vector<int> start = {3, 0};
  vector<int> endP = {3, 3};
  path.insert({start, {}});

  // 先插入默认的起点
  map.insert({0, start});

  auto check = [&](int x, int y) -> bool {
    bool reach = false;
    reach = reach || x < 0 || x >= int(vec.size()); // x 越界
    reach = reach || y < 0 || y >= int(vec[0].size()); // y 越界
    reach = reach || vec[x][y] != 0;                   // 该点已经被搜查过
    reach = reach || (x == start[0] && y == start[1]);               // 起点
    return reach;
  };

  auto setPath = [&](auto p, int x, int y, int weight) -> bool {
    vector<int> pos = {x, y};
    if (!check(x, y)) {
      vec[x][y] = weight; // 设置weight
      map.insert({weight, pos}); // 插入待搜索map
      auto parentPath = path.at(p);
      parentPath.push_back(p);
      path.insert({pos, parentPath});
      count++;
    }
    return pos == endP;
  };

  // 搜索周围点
  auto search = [&](std::vector<int> &p, int weight) -> bool {
    int x(p[0]), y(p[1]);
    bool isFind = false;
    isFind = isFind || setPath(p, x + 1, y, weight + 1);
    isFind = isFind || setPath(p, x - 1, y, weight + 1);
    isFind = isFind || setPath(p, x , y + 1, weight + 1);
    isFind = isFind || setPath(p, x, y - 1, weight + 1);
    return isFind;
  };

  while (!map.empty()) {
    // 先获取G值最小的遍历
    auto it = map.begin();
    auto weight = it->first;
    auto pos = it->second;
    // 将遍历过的删除
    map.erase(it);
    // 将遍历过的坐标设置为3
    vec[pos[0]][pos[1]] = weight;
    
    // 移动当前坐标
    if (search(pos, weight)) {
      break;
    }
  }

  for (unsigned i = 0; i < vec.size(); i++) {
    for (unsigned j = 0; j < vec[i].size(); j++) {
      std::cout.width(2);
      std::cout << vec[i][j] << " ";
    }
    std::cout << "\n";
  }
  std::cout << "起点: (" << start[0] << ", " << start[1] << ")\n";
  std::cout << "终点: (" << endP[0] << ", " << endP[1] << ")\n";
  std::cout << "搜索次数: " << count << "\n";
  std::cout << "最短路径: ";
  for (auto line : path.at(endP)) {
    std::cout << "(" << line[0] << ", " << line[1] << ") ";
  }
  std::cout << "(" << endP[0] << ", " << endP[1] << ")\n";
  // yinfo << path;
  std::cout << "\n";
}

int main() {
  vector<vector<int>> vec = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, -1, -1, -1, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };
  ASearch(vec);
  return 0;
}