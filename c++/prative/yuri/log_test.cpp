/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2025-10-16 08:42:21
 * @Description: 日志测试测试
 */

#include "yuri_log.hpp"

#include <iostream>
#include <chrono>
#include <thread>
#include <atomic>

std::atomic<int> counter{0};

void log_test_thread() {
  auto start = std::chrono::steady_clock::now();
  while (true) {
    // 写入不同类型的日志
    yerror << "yuri is yes";

    counter++;

    // 检查是否已经运行了1秒
    auto now = std::chrono::steady_clock::now();
    if (now - start >= std::chrono::seconds(1)) {
      break;
    }
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  
  yuri::Log::writeMode() = yuri::Log::WriteInConsole;
  
  // 启动测试线程
  std::thread t(log_test_thread);

  // 等待测试完成
  t.join();

  // 输出结果
  std::cout << "Logs written in 1 second: " << counter << std::endl;
  return 0;
}