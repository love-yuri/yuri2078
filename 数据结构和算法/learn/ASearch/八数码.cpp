/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-11 22:00:25
 * @LastEditTime: 2024-06-12 11:42:04
 * @Description: 八数码问题-A*算法
 */

#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <queue>
#include <vector>
#include <memory>

using std::vector;

// 地图上的点-这里是八数码转int的值
// 列如 123 456 780 转成 12345678
struct Point {
  std::shared_ptr<Point> parent; // 父节点
  int val;   // 八位数码的值
  int h;     // 启发式函数值
  int g;     // 移动代价

  // 3 * 3 地图中的xy坐标
  int x;
  int y;

  // 禁止隐式转换
  explicit Point(int val) noexcept :
    parent(nullptr), val(val), h(0), g(0), x(0), y(0) {
  }

  // 拷贝构造
  Point(const Point &p) noexcept :
    parent(p.parent), val(p.val), h(p.h), g(p.g), x(p.x), y(p.y) {
  }

  // 重载等于符号
  bool operator==(const Point &p) const {
    return this->val == p.val;
  }

  // 获取估价函数的值
  int F() const {
    return h + g;
  }

  // 重载小于符号-用于设置优先队列
  bool operator<(const Point &p) const {
    return this->F() > p.F();
  }
};

// 重载<< 方便观察输出
std::ostream &operator<<(std::ostream &cout, const Point &p) {
  int val = p.val;
  vector<int> martix(9);
  for (int i = 0; i < 9; i++) {
    martix[i] = val % 10;
    val /= 10;
  }
  for (int i = 2; i >= 0; i--) {
    for (int j = 2; j >= 0; j--) {
      cout << martix[i * 3 + j] << " ";
    }
    cout << "\n";
  }
  return cout;
}

class ASearch {
  vector<vector<int>> map;         // 地图数据
  std::priority_queue<Point> open; // open表
  std::unordered_set<int> close;   // close表，存放已经访问过的点
  Point target;                    // 目标状态
  Point start;                     // 起始状态
  int count;                       // 计数

public:
  ASearch(const vector<vector<int>> &map, const vector<vector<int>> &target) :
    map(map), target(MapToPoint(target)), start(MapToPoint(map)), count(0) {
  }

  // 开始搜索
  void Search() {
    // 添加起点作为初始元素
    open.push(start);
    close.insert(start.val);

    while (!open.empty()) {
      // 取出f值最小的点
      Point p = open.top();
      open.pop();

      // 判断是否到达目标
      if (p == target) {
        std::cout << "找到目标: 共计查找 " << count << " 个点\n";
        getPath(p);
        break;
      }

      // 进行扩展
      moveToNext(p);
    }
  }

  void getPath(const Point &p) {
    // 获取路径
    if (p.parent) {
      getPath(*p.parent.get());
    }
    std::cout << p << "\n";
  }

  // 将点的信息转为地图信息
  void setMap(const Point &p) {
    int val = p.val;
    for (int i = 2; i >= 0; i--) {
      for (int j = 2; j >= 0; j--) {
        map[i][j] = val % 10;
        val /= 10;
      }
    }
  }

  // 判断是否能添加到queue
  void addToQueue(Point &p, unsigned x, unsigned y) {
    // 先判断该点是否可达
    if (x < 0 || x >= map.size() || y < 0 || y >= map[0].size()) {
      return;
    }
    // 先交换两个点
    std::swap(map[p.x][p.y], map[x][y]);
    Point next(MapToPoint(map));
    // 如果他没有在close表中，则添加到open表中
    if (!close.contains(next.val)) {
      next.parent = std::make_shared<Point>(Point(p)); // 添加父路径
      next.g = p.g + 1; // 默认g值是原点 + 1，因为一次只能移动1格
      next.h = getH(next);
      open.push(next); // 添加到open表中
      close.insert(next.val); // 添加到close表中，表示已经遍历完毕
    }
    // 将地图回复至原状
    std::swap(map[p.x][p.y], map[x][y]);
  }

  void moveToNext(Point &p) {
    // 上下左右移动
    setMap(p);
    count++;
    addToQueue(p, p.x + 1, p.y);
    addToQueue(p, p.x - 1, p.y);
    addToQueue(p, p.x, p.y + 1);
    addToQueue(p, p.x, p.y - 1);
  }

  // 获取h值
  int getH(const Point &p) {
    int val = p.val;
    int tar = target.val;
    int h = 0;
    while (val != 0) {
      if (val % 10 != tar % 10) {
        h++;
      }
      val /= 10;
      tar /= 10;
    }
    return h;
  }

  // 将地图数据转换成Point数据
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
  // 起始地图
  const vector<vector<int>> map = {
    {2, 8, 3},
    {1, 6, 4},
    {7, 0, 5},
  };
  // 目标地图
  const vector<vector<int>> target = {
    {1, 2, 3},
    {8, 0, 4},
    {7, 6, 5},
  };
  ASearch search(map, target);
  search.Search();
  return 0;
}