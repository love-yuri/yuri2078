/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-11 21:42:29
 * @LastEditTime: 2023-12-11 22:33:31
 * @Description: 时间片调度模拟
 */
#include <chrono>
#include <iostream>
#include <string>
#include <thread>
#include <yuri_log.hpp>
#include <queue>

/* 默认时间片大小 */
#define TIME_SLICE 3

enum State {
  READY, // 就绪
  RUNNING, // 运行
  FINISHED, // 完成
};

typedef struct {
  std::string name; // 任务名字
  State state; // 进程状态
  int ntime;   // 需要时间片
  int rtime; // 已经运行时间片
} Pcb;

/* 任务队列 */
std::queue<Pcb> readyQueue;
void createTask() {
  Pcb pcb;
  std::cout << "请输入任务名称: ";
  std::cin >> pcb.name;
  std::cout << "请输入任务需要时间片: ";
  std::cin >> pcb.ntime;
  pcb.state = READY;
  pcb.rtime = 0;
  readyQueue.push(pcb);
}

void destory(Pcb &pcb) {
  info << pcb.name << " 已完成, 共计消耗 -> " << pcb.rtime << " 个时间片";
  pcb.state = FINISHED;
}

void running() {
  while (!readyQueue.empty()) {
    Pcb &pcb = readyQueue.front();
    readyQueue.pop();
    pcb.state = RUNNING;
    for (int i = 0; i < TIME_SLICE; i++) {
      if (pcb.rtime < pcb.ntime) {
        pcb.rtime++;
        info << pcb.name << " 正在运行";
      } else {
        destory(pcb);
        break;
      }
      std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    if (pcb.state == RUNNING) {
      pcb.state = READY;
      readyQueue.push(pcb);
    }
  }
}
int main() {
  int num(0);
  std::cout << "请输入需要添加任务数量: ";
  std::cin >> num;
  for (int i = 0; i < num; i++) {
    createTask();
  }
  running();
  info << "全部完成!";
  return 0;
}

