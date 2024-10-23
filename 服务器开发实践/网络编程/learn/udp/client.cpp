/*
 * @Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @Date: 2024-10-10 14:05:51
 * @LastEditTime: 2024-10-22 11:57:23
 * @Description:
 */
#include "UdpClient.h"
#include <thread>
#include <yuri/yuri_log.hpp>

int main() {
  UdpClient client(2079);
  std::thread thread;
  thread = std::thread([&client]() {
    while (true) {
      if (client.recvFrom() == "") {
        error << "get message error!";
        return;
      }
    }
  });

  info << "线程 id -> " << std::this_thread::get_id();

  while (true) {
    std::string msg;
    std::cin >> msg;
    if (msg == "bye") {
      break;
    }

    client.sendTo(msg);
    info << "发送 -> " << msg;
  }

  if (thread.joinable()) {
    thread.join();
  }
  return 0;
}