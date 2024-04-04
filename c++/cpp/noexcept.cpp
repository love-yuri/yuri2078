/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-04-04 20:08:59
 * @LastEditTime: 2024-04-04 20:35:37
 * @Description: noexcept 学习
 */
#include <yuri/yuri_log.hpp>

/* 懒得打y */
#define info yinfo
#define error yerror

/*
 * noexcept 是 C++11 新增的，用来表示函数不会抛出异常
 * 一个函数不加任何修饰默认是 noexcept(false) 的也就是会抛出异常
 * noexcept 是运算符 - 修饰符 c17起作为函数的修饰符
 * 使用原则： 能用就用，保证不抛出异常就可以加上
 * url: https://zh.cppreference.com/w/cpp/language/noexcept
 */

/* 默认是 noexcept, 等同于 noexcept(false) */
void fun() {
  info << "hello";
}

// 安全
void fun_safe() noexcept {
  info << "hello";
}

// 不能作为函数重载的一部分
// void fun() noexcept {
//   info << "hello";
// }

// 也可以是这种形式的
void fun_test() noexcept(noexcept(fun_safe())) {
  info << "hello ";
}

int main() {
  info << std::boolalpha << "函数是否会抛出异常 -> " << noexcept(fun());
  info << std::boolalpha << "函数是否会抛出异常 -> " << noexcept(fun_safe());
  info << std::boolalpha << "函数是否会抛出异常 -> " << noexcept(2);

  return 0;
}