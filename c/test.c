/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2023-11-21 21:16:53
 * @Description:
 */
#include <stdio.h>
#include <malloc.h>
typedef struct LNode {
  int data;
  struct LNode *next;
} LNode, *LinkList;
// 初始化
int InitList(LinkList *L) {
  *L = (LNode *) malloc(sizeof(LNode *)); // 为头节点分配空间
  if (L == NULL)                        // 分配失败
    return 0;
  (*L)->next = NULL;
  return 1;
}
// 按位序插入
int ListInsert(LinkList L, int i, int e) {
  if (i < 1)
    return 0;
  LNode *p;
  int j = 0;
  p = L;
  while (p != NULL && j < i - 1) {
    p = p->next;
    j++;
  }
  if (p == NULL)
    return 0;
  LNode *s = (LNode *)malloc(sizeof(LNode));
  s->data = e;
  s->next = p->next;
  p->next = s;
  return 1;
}
int main() {
  /* 链表初始化 */
  LinkList head = (LinkList)calloc(0, sizeof(LNode));
  head->next = NULL;
  // (2)
  InitList(&head);
}