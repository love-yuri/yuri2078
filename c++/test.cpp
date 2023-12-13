/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2023-11-21 21:14:33
 * @Description:
 */

#include <stdio.h>
#include <stdlib.h>
#define getpch(type) (type *)malloc(sizeof(type))

struct pcb {                       // 定义进程控制块
  char name[10];                   // 进程的名字
  char state;                      // 进程的状态
  int count;                       // 进程优先级
  int ntime;                       // 进程运行需要的CPU时间
  int rtime;                       // 进程已运行的时间
  struct pcb *link;                // 连接pcb的指针
} *ready = NULL, *tail = NULL, *p; // 就绪队列指针，队尾指针
typedef struct pcb PCB;
int slice = 1;

PCB *readyMaxProcess;
int readyQueNum = 0; // 就绪队列的进程数量

void sort() // 将进程插入到就绪指针
{
  PCB *q;
  if (ready == NULL) // 队列为空，将p插入到队列中
  {
    ready = p;
    tail = p;
  } else // 若就绪队列不为空，将p插入到队列
  {
    if (p->count > ready->count) // p指针所指节点的count值头的大于队列节点的count值，将p指针所指节点插入到对头
    {
      p->link = ready;
      ready = p;
    } else {
      bool m = false;
      q = ready;
      // q2=q1->link;
      while (m == false) {
        if (tail->count >= p->count) // 若p的count值小于队尾指针所指节点的的count值的话，将p插到队尾
        {
          tail->link = p;
          tail = p;
          p->link = NULL;
          m = true;
        } else {
          if (q->count >= p->count && p->count > q->link->count) // 若p的count值大于队尾指针所指节点的的count值的话,将p所指节点插入到队列中指定位置
                                                                 // 必须满足插入位置的前一个节点的count值大于p->count,并且满足插入位置的后一个节点的count值小于p->count
          {
            p->link = q->link;
            q->link = p;
            m = true;
          } else {
            q = q->link;
            // q2=q2->link;
          }
        }
      }
    }
  }
}

// 输入进程信息
void input() {
  int i, num;
  printf("\n 请输入进程个数:");
  scanf("%d", &num);
  for (i = 0; i < num; i++) {
    printf("\n 进程号No.%d:\n", i);
    p = getpch(PCB);
    printf("\n 请输入进程名:");
    scanf("%s", p->name);

    printf("\n 请输入进程优先权数:");
    scanf("%d", &p->count);

    printf("\n 请输入进程运行时间:");
    scanf("%d", &p->ntime);
    printf("\n");
    p->rtime = 0;
    p->state = 'w';
    p->link = NULL;
    sort(); // 将进程p插入就绪队列ready中
  }
  printf("\n 请输入时间片大小:");
  scanf("%d", &slice);
}

// 获得就绪队列中进程的个数
int space() {
  PCB *pr = ready;
  while (pr != NULL) {
    readyQueNum++;
    pr = pr->link;
  }
  return (readyQueNum);
}

// 显示进程
void disp(PCB *pr) {
  printf("\nqname \tstate \tcount \tndtime \truntime \n");
  printf("|%s\t", pr->name);
  printf("|%c\t", pr->state);
  printf("|%d\t", pr->count);
  printf("|%d\t", pr->ntime);
  printf("|%d\t", pr->rtime);
  printf("\n");
}

// 显示当前运行进程和就绪队列中进程的信息
void check() {
  PCB *pr;
  printf("\n **** 当前正在运行的进程是:%s", readyMaxProcess->name);
  disp(readyMaxProcess);
  pr = ready;
  printf("\n ****当前就绪队列状态为:\n");
  while (pr != NULL) {
    pr->count++;
    disp(pr);
    pr = pr->link;
  }
}

// 撤销进程
void destroy() {
  printf("\n 进程 [%s] 已完成.\n", readyMaxProcess->name);
  free(readyMaxProcess);
  // readyQueNum--;
}

// 使当前进程运行一个时间片，若结束则撤销，否则插入就绪队列队尾
void running() {
  int tempt = 0;
  tempt = readyMaxProcess->ntime - readyMaxProcess->rtime;
  if (tempt > slice)
    readyMaxProcess->rtime += slice;
  else
    readyMaxProcess->rtime += tempt;

  check();
  if (readyMaxProcess->rtime == readyMaxProcess->ntime)
    destroy();
  else {
    readyMaxProcess->count = readyMaxProcess->count - 3;
    readyMaxProcess->state = 'w';
    p = readyMaxProcess; // 再将队头节点readyMaxProcess插入到队列时，现将赋给另一个指针p
    sort();
  }
}

int main() {
  int len, h = 0;
  input();                              // 输入进程并形成就绪队列
  len = space();                        // 获得就绪队列中进程的个数
  while ((len != 0) && (ready != NULL)) // 若就绪队列不为空
  {
    len = space();
    h++;
    printf("\n The execute number:%d \n", h);
    readyMaxProcess = ready;      // 将指向队优先级最大的节点的指针指向队头节点
    ready = ready->link;          // 改变对头指针
    readyMaxProcess->link = NULL; // 将优先级最大的进程从队列中分裂出来
    readyMaxProcess->state = 'R';
    running();
  }
  printf("\n\n 所有进程已经完成.\n");
}