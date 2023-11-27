/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-27 14:43:23
 * @LastEditTime: 2023-11-27 14:43:25
 * @Description:
 */
#include <stdio.h>
#include <unistd.h>

int main() {
  pid_t pid = fork();
  if (pid == 0) {
    // 子进程执行的代码
    exit(0);
  }
  int status = 0;
  waitpid(pid, &status, 0);
  printf("子进程退出状态：%d\n", status);
  return 0;
}