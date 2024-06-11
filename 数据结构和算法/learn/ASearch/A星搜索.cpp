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
using std::map;

class ASearch {
  vector<vector<int>> map;                         // 地图
  std::map<vector<int>, vector<vector<int>>> path; // 最终生成的路径
  multimap<int, vector<int>> weightMap;            // 权重map
  vector<int> start;                               // 起点
  vector<int> end;                                 // 终点
  int count;                                       // 计数器

  using Point = const std::vector<int> &;

public:
  ASearch(Point start, Point end, vector<vector<int>> &map) :
    map(map), start(start), end(end), count(1) {
    path.insert({start, {}});
    weightMap.insert({0, start});
  }

  bool check(int x, int y) {
    bool reach = false;
    reach = reach || x < 0 || x >= int(map.size());    // x 越界
    reach = reach || y < 0 || y >= int(map[0].size()); // y 越界
    reach = reach || map[x][y] != 0;                   // 该点已经被搜查过
    reach = reach || (x == start[0] && y == start[1]); // 起点
    return reach;
  };

  int getWeight(Point p, int g) {
    return g + (abs(end[0] - p[0]) + abs(end[1] - p[1]));
  }

  bool setPath(auto p, int x, int y, int weight) {
    vector<int> pos = {x, y};
    if (!check(x, y)) {
      map[x][y] = getWeight(pos, weight);              // 设置weight
      weightMap.insert({weight, pos}); // 插入待搜索map
      auto parentPath = path.at(p);
      parentPath.push_back(p);
      path.insert({pos, parentPath});
      count++;
    }
    return pos == end;
  };

  bool search(std::vector<int> &p, int weight) {
    int x(p[0]), y(p[1]);
    bool isFind = false;
    isFind = isFind || setPath(p, x + 1, y, weight + 1);
    isFind = isFind || setPath(p, x - 1, y, weight + 1);
    isFind = isFind || setPath(p, x, y + 1, weight + 1);
    isFind = isFind || setPath(p, x, y - 1, weight + 1);
    return isFind;
  };

  void startToSearch() {
    // 搜索周围点

    while (!weightMap.empty()) {
      // 先获取G值最小的遍历
      auto it = weightMap.begin();
      auto weight = it->first;
      auto pos = it->second;
      // 将遍历过的删除
      weightMap.erase(it);
      // 将遍历过的坐标设置为3
      map[pos[0]][pos[1]] = weight;

      // 移动当前坐标
      if (search(pos, weight)) {
        break;
      }
    }

    for (unsigned i = 0; i < map.size(); i++) {
      for (unsigned j = 0; j < map[i].size(); j++) {
        std::cout.width(2);
        std::cout << map[i][j] << " ";
      }
      std::cout << "\n";
    }
    std::cout << "起点: (" << start[0] << ", " << start[1] << ")\n";
    std::cout << "终点: (" << end[0] << ", " << end[1] << ")\n";
    std::cout << "搜索次数: " << count << "\n";
    std::cout << "最短路径: ";
    for (auto line : path.at(end)) {
      std::cout << "(" << line[0] << ", " << line[1] << ") ";
    }
    std::cout << "(" << end[0] << ", " << end[1] << ")\n";
    // yinfo << path;
    std::cout << "\n";
  }
};

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
  ASearch s({3, 0}, {3, 3}, vec);
  s.startToSearch();
  return 0;
}