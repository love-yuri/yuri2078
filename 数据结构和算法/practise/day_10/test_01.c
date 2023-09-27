#include<stdio.h>
#include <stdlib.h>

#define INITSIZE 1000
#define INCRE 20
#define OK 1
#define ERROR 0

typedef struct{
  char* data;
  int length,stringsize;
}SqString;

//串初始化
int initString(SqString* S)
{
	S->data = (char *)calloc(INITSIZE,sizeof(char));
    if(!S->data){
        return ERROR;
    }
    S->length = 0;
    S->stringsize = INITSIZE;
    return OK;
}

//串赋值
int strAssign(SqString* s, char* str)
{
	int i = 0;
    for(i = 0; *str; i++)
    {
        if(i > s->stringsize - 2){
            return ERROR;
        }
        s->data[i] = *str;
        str++;
    }
    s->data[i] = 0;
    s->length = i;
    return OK;
}
//模式匹配KMP算法
int indexKMP(SqString* s, SqString* t, int next[])
{
	if (t->length == 0) {
		return 0;
	}
	for (int i = 0, j = 0; i < s->length; i++) {
		if (s->data[i] == t->data[j]) {
			j++;
        }else if (next[j]) {
			j = next[j];
			i--;
        }else {
            j = next[j];
		}

		if (!t->data[j]) {
			int k = i - j + 1;
			while (s->data[k + t->length]) {
				s->data[k] = s->data[k + t->length];
				k++;
			}
			s->data[k] = 0;
			s->length -= t->length;
			indexKMP(s, t, next);
			return i - j + 2;
        }
    }
	return -1;
}
//求取模式串next值
void getNext(SqString* t, int next[])
{
	next[0] = 0;
	for (int i = 1; i < t->length; i++) {
		if (t->data[i] == t->data[next[i - 1]]) {
			next[i] = next[i - 1] + 1;
        }else {
			int j = next[i - 1] - 1;
			while (j >= 0 && t->data[j] != t->data[i]) {
                j--;
			}
			next[i] = j + 1;
        }
	}
}

// int my_gets(char* str)
// {
// 	char ch;
// 	int i = 0;
// 	while ((ch = getchar()) != '\n') {
// 		str[i++] = ch;
// 	}
// 	str[i] = 0;
// 	return i;
// }

int main()
{
	//使用KMP算法完成串的模式匹配
	SqString s, t;
	initString(&s);
	initString(&t);

	char* str = (char*)calloc(INITSIZE, sizeof(char));
	gets(str);
	strAssign(&s, str);
	gets(str);
	strAssign(&t, str);
	int* next = (int*)calloc(t.length, sizeof(int));
	getNext(&t, next);
	indexKMP(&s, &t, next);
	puts(s.data);
	
	return 0;
}
