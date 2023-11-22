/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-13 14:59:53
 * @LastEditTime: 2023-11-13 15:01:02
 * @Description: test
 */
#include <iostream>
#include <unistd.h>

int main() {
  pid_t childPid = fork();

  if (childPid == -1) {
    // 错误处理
    std::cerr << "Fork failed!" << std::endl;
    return 1;
  } else if (childPid == 0) {
    // 子进程代码
    std::cout << "This is the child process." << std::endl;
  } else {
    // 父进程代码
    std::cout << "This is the parent process. Child PID: " << childPid << std::endl;
  }

  return 0;
}
