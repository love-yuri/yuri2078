# A*搜索算法

> 本文是基于 [哔哩哔哩 ](https://www.bilibili.com/video/BV1bv411y79P/?spm_id_from=333.337.search-card.all.click) 和 [CSDN](https://blog.csdn.net/a_vegetable/article/details/115361888)  的理解



## 什么是A*搜索算法?

> 当我们需要在静态网络中(可以是图可以是网格)求解出一个有效路径时，我们就可以使用A*搜索算法。但是A\*算法并不保证能够获取到最短的路径

那么他的具体步骤是什么呢？

1. 首先我们从起点出发，将起点的最短距离(weight) 设置为0，因为自己到自己就是0。并将起点添加到待搜索的点(此时只有1个)

   > 因为，加入a - c的最短路径经过 b， 那么 a - b的路径也要是最短的。

2. 从待搜索的点中找到权重最小的。并搜索他能到达的点，因为这个点的权重最小，那么他能到的点也必然是权重最小的

3. 将最小点能到的点并且并没有被搜索过点加入到待搜索的点中(因为如果该点已经被搜索过就说明你再过去便不再是最短路径了)

4. 将最小点从待搜索的列表中移除

5. 重复2 - 4步直到遍历完成整个图获取找到了终点

那么以上和dijkstra 有什么区别呢，区别就是权重这个东西。在dijkstra中他是一个固定的值。

但是在A*中他是由两个部分组成

`F = G + H `

这里的F称作启发函数，F(n): n就是某个点，他的结果我们可以理解为在某轮计算中起点a 到 点n的权重

G 是点 a 移动到点n 本身的代价

H 是点n 到终点的代价（这个代价可以用曼哈顿距离或者欧氏距离表示）

用启发函数的结果替代第二步中权重最小的值，就是最后a*算法的步骤了

那么这个算法和dijkstra有什么区别呢。

当H 的值永远为0，也就是只依靠起点到n的距离来选择下一个点，此时a*算法就退化成dijkstra算法。我们来看个例子

## 案例1

> 在 8 \* 8 的无障碍地图中，给定一个起点，终点，求起点到终点的最短路径

```c++
// 定义地图
vector<vector<int>> vec = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };

vector<int> start = {2, 1}; // 起点
vector<int> endP = {6, 3}; // 终点
```

### 开始

假设我们设置起点为 2 1， 我们要找到从2 1 到 6 3 的一条路径，执行代码后我们发现，右下角的部分是没有遍历到的，在遍历了一半的地图时他就结束了遍历。一共进行了39次搜索。

```
 // 数字为0代表没有被检索到，> 0 表示起点到该点的最小权重。 起点默认是0
 3  2  3  4  5  0  0  0 
 2  1  2  3  4  5  0  0 
 1  0  1  2  3  4  5  0 
 2  1  2  3  4  5  0  0 
 3  2  3  4  5  0  0  0 
 4  3  4  5  0  0  0  0 
 5  4  5  6  0  0  0  0 
 6  5  6  0  0  0  0  0 
起点: (2, 1)
终点: (6, 3)
搜索次数: 39
最短路径: (2, 1) (3, 1) (4, 1) (5, 1) (6, 1) (6, 2) (6, 3)
```

而在我们把终点改成 6 7时, 他几乎遍历完了整个表。所以此时算法的效率很低

```c++
 3  2  3  4  5  6  7  8 
 2  1  2  3  4  5  6  7 
 1  0  1  2  3  4  5  6 
 2  1  2  3  4  5  6  7 
 3  2  3  4  5  6  7  8 
 4  3  4  5  6  7  8  9 
 5  4  5  6  7  8  9 10 
 6  5  6  7  8  9 10  0 
起点: (2, 1)
终点: (6, 7)
搜索次数: 62
最短路径: (2, 1) (3, 1) (4, 1) (5, 1) (6, 1) (6, 2) (6, 3) (6, 4) (6, 5) (6, 6) (6, 7)
```



### 完整代码

```c++
#include <map>
#include <vector>
#include <iostream>

/**
 * A* search algorithm in C++
 * 通过a*算法在C++中找到结果
 */

// #include <iostream>
// #define yinfo std::cout

using std::vector;
using std::multimap;

auto ASearch(vector<vector<int>> &vec) {
  int count = 0;
  // 待搜索的map， key是G， value是下表
  multimap<int, vector<int>> map = multimap<int, vector<int>>();
  // 存储最短路径
  std::map<vector<int>, vector<vector<int>>> path;

  vector<int> start = {2, 1};
  vector<int> endP = {6, 3};
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
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };
  ASearch(vec);
  return 0;
}
```

## 案例2

加入我们给他来一堵墙, 让他搜搜 3 0 -> 3 3的路径

```c++
  vector<vector<int>> vec = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, -1, -1, -1, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };
```

在没有墙时:

```
 3  0  0  0  0  0  0  0 
 2  3  0  0  0  0  0  0 
 1  2  3  0  0  0  0  0 
 0  1  2  3  0  0  0  0 
 1  2  3  0  0  0  0  0 
 2  3  0  0  0  0  0  0 
 3  0  0  0  0  0  0  0 
 0  0  0  0  0  0  0  0 
起点: (3, 0)
终点: (3, 3)
搜索次数: 15
最短路径: (3, 0) (3, 1) (3, 2) (3, 3)
```

有墙时:

```
 3  4  5  6  7  8  9 10 
 2  3 -1 -1 -1  9 10  0 
 1  2 -1  0  0 10  0  0 
 0  1 -1 11  0  0  0  0 
 1  2 -1 10  0  0  0  0 
 2  3 -1  9 10  0  0  0 
 3  4 -1  8  9 10  0  0 
 4  5  6  7  8  9 10  0 
起点: (3, 0)
终点: (3, 3)
搜索次数: 36
最短路径: (3, 0) (4, 0) (5, 0) (6, 0) (7, 0) (7, 1) (7, 2) (7, 3) (6, 3) (5, 3) (4, 3) (3, 3)
```

我们发现，有墙时他搜索的很慢，在几乎快遍历完了所有点后才找到答案

## 案例3

假设我们的地图长这样

```
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
```

他直接 (3, 0) (4, 0) (4, 1) (4, 2) (4, 3) (3, 3) 就能找到终点,但我们看它实际遍历的地图,发现其实最底下他都可以不用的去的，但是他却遍历了。此时就需要我们的启发函数中的H出现了，因为我们上帝视角知道从第五行就可以过去。

```
 3  4  0  0  0  0  0  0 
 2  3 -1 -1 -1  0  0  0 
 1  2 -1  0  0  0  0  0 
 0  1 -1  5  0  0  0  0 
 1  2  3  4  0  0  0  0 
 2  3 -1  5  0  0  0  0 
 3  4 -1  0  0  0  0  0 
 4  5  0  0  0  0  0  0 
```

