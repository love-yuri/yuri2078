/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-13 14:40:49
 * @LastEditTime: 2023-11-13 14:55:37
 * @Description: 多进程创建测试
 */
#include <iostream>
#include <unistd.h>

int main() {
  int i;
  for (i = 0; i < 3; i++) {
    int pid = fork();
    if (pid == 0) {
      break;
    }
  }
  sleep(i);
  if (i < 3) {
    printf("I am child:%d my parent:%d\n", getpid(), getppid());
  } else {
    printf("I am parent:%d\n", getpid());
  }
  return 0;
}