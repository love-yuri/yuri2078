/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-27 15:03:03
 * @LastEditTime: 2023-11-27 15:04:15
 * @Description:
 */
#include <cstdlib>
#include <iostream>
#include <sched.h>
#include <yuri_log.hpp>
#include <unistd.h>
#include <sys/wait.h>
int main() {
  info << "程序开始运行!!! 当前pid -> " << getpid();
  pid_t pid = fork();

  if (pid == 0) {
    info << "当前是子进程: pid -> " << getpid() << " 父进程 -> " << getppid();
    std::system("ls");
  } else {
    info << "当前是父进程: pid -> " << getpid() << " 子进程 -> " << pid;
    waitpid(pid, nullptr, 0);
  }
  return 0;
}