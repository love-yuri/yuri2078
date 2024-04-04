/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-04-04 21:02:11
 * @LastEditTime: 2024-04-04 21:24:26
 * @Description: lambda的使用
 */

#include <yuri/yuri_log.hpp>

/**
 * lambda 是一个无名的 非聚合类
 * lambda 是一个类, 他重载了 operator()
 * url: https://zh.cppreference.com/w/cpp/language/lambda
 */

// #include <iostream>
// #define yinfo std::cout

int main() {
  const auto fun = [] {
    yinfo << "hello world";
  };
  fun();
  return 0;
}