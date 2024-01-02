/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2023-11-24 08:41:15
 * @Description: 堆排序
 */
#include <iostream>
#include <vector>
#include <yuri.h>

yuri::Yuri init; // 读取数据类

// v 保存着需要建堆的元素个数
// 建立大顶堆： 跟节点大于等于他的所有叶子节点
// 类似完全二叉树
void heapAdjust(std::vector<int> &list, int v) {
  // 从右往左从下往上，先找到第一个有孩子的节点
  // 这个节点的坐标是v（size） / 2 - 1
  // 然后交换节点与孩子建堆
  for (int k = v / 2 - 1; k >= 0; k--) {
    int lchild = 2 * k + 1; // 节点的左孩子
    int rchild = 2 * k + 2; // 节点的右孩子
    int next = 0;           // 设置根节点最大的孩子节点

    // 如果此时没有右节点或者 左孩子的值大于右孩子
    // 那么接下来需要比较的节点就是左孩子，否则为右孩子
    if (rchild >= v || list[lchild] > list[rchild]) {
      next = lchild;
    } else {
      next = rchild;
    }

    // 如果根节点的值 小于最大子节点 则进行交换
    // 并且更新父节点为交换的子节点
    if (list[k] < list[next]) {
      std::swap(list[k], list[next]);
    }
  }
  init.outData();

  // 交换根节点（最大值） 与 最后一个节点的值，类似选择排序
  std::swap(list[0], list[v - 1]);
}

// 堆排序： 建堆，然后将根节点元素与最后一个节点交换
// 然后将剩余节点继续建堆，再将根节点与最后一个节点交换（最后一个不算之前的最后
void heapSort(std::vector<int> &data) {
  init.cleanLog();
  init.outData();
  const int n = data.size();
  for (int i = 0; i < n - 1; i++) {
    init << "第 " << i + 1 << " 次建堆 : \n";
    heapAdjust(data, n - i);
  }
}

int main() {
  std::vector<int> &data = init.getData(true);
  heapSort(data);
  init.outData();
  return 0;
}