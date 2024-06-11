/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-11 22:00:25
 * @LastEditTime: 2024-06-11 23:40:18
 * @Description: 八数码问题-A*算法
 */

#include <iostream>
#include <unordered_set>
#include <queue>
#include <vector>

using std::vector;
using std::cout;

// 地图上的点-这里是八数码转int的值
// 列入 123 456 780 转成 12345678
struct Point {
  Point *parent; // 父节点
  int val;       // 八位数码的值
  int h;         // 启发式函数值
  int g;         // 实际距离

  // 3 * 3 地图中的xy坐标
  int x;
  int y;

  Point(int val) :
    parent(nullptr), val(val), h(0), g(0), x(0), y(0) {
  }

  // 重载等于符号
  bool operator==(const Point &p) const {
    return this->val == p.val;
  }

  // 获取股价函数的值
  int F() const {
    return h + g;
  }

  // 重载小于符号-用于设置优先队列
  bool operator<(const Point &p) const {
    return this->F() < p.F();
  }
};

class ASearch {
  vector<vector<int>> map;         // 地图数据
  std::priority_queue<Point> open; // open表
  std::unordered_set<int> close;   // close表，存放已经访问过的点
  Point target;                    // 目标状态
  Point start;                     // 起始状态

public:
  ASearch(const vector<vector<int>> &map, const vector<vector<int>> &target) :
    map(map), target(MapToPoint(target)), start(MapToPoint(map)) {
  }

  // 开始搜索
  void Search() {
    // 添加起点作为初始元素
    open.push(start);

    while (!open.empty()) {
      // 取出f值最小的点
      Point p = open.top();
      open.pop();
      close.insert(p.val);

      // 判断是否到达目标
      if (p == target) {
        cout << "找到目标";
        break;
      }

      // 进行扩展
      moveToNext(p);
    }
  }

  // 判断是否能添加到queue
  void addToQueue(Point &p, unsigned x, unsigned y) {
    if (x < 0 || x >= map.size() || y < 0 || y >= map[0].size()) {
      return;
    }
    // 上下左右移动
    std::swap(map[p.x][p.y], map[x][y]);
    Point next(MapToPoint(map));
    if (!close.contains(next.val)) {
      next.parent = &p;
      next.g = p.g + 1;
      next.h = getH(next);
      open.push(next);
    }
    std::swap(map[p.x][p.y], map[x][y]);
  }

  void moveToNext(Point &p) {
    addToQueue(p, p.x + 1, p.y);
    addToQueue(p, p.x - 1, p.y);
    addToQueue(p, p.x, p.y + 1);
    addToQueue(p, p.x, p.y - 1);
  }

  int getH(const Point &p) {
    int val = p.val;
    int tar = target.val;
    int h = 8;
    while (val != 0) {
      if (val % 10 == tar % 10) {
        h--;
      }
      val /= 10;
      tar /= 10;
    }
    return h;
  }

  Point MapToPoint(const vector<vector<int>> &vec) {
    // 把地图上的点转成Point
    Point p(0);
    for (unsigned i = 0; i < vec.size(); i++) {
      for (unsigned j = 0; j < vec[i].size(); j++) {
        p.val = p.val * 10 + vec[i][j];
        if (vec[i][j] == 0) {
          p.x = i;
          p.y = j;
        }
      }
    }
    return p;
  }
};

int main() {
  const vector<vector<int>> map = {
    {2, 8, 3},
    {1, 6, 4},
    {7, 0, 5},
  };
  const vector<vector<int>> target = {
    {1, 2, 3},
    {8, 0, 4},
    {7, 6, 5},
  };
  ASearch search(map, target);
  search.Search();
  return 0;
}