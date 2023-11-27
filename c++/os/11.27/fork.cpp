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
    int status = 0;
    info << "当前是子进程: pid -> " << getpid() << " 父进程 -> " << getppid();
    std::cout << "请输入返回信息: ";
    std::cin >> status;
    exit(status);
  } else {
    int status = 0;
    info << "当前是父进程: pid -> " << getpid() << " 子进程 -> " << pid;
    waitpid(pid, &status, 0);
    int result = WEXITSTATUS(status);
    info << "父进程退出 msg -> " << result;
  }
  return 0;
}