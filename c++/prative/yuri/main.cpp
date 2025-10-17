/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2025-10-17 16:39:42
 * @Description: 测试
 */

#include "yuri_log.hpp"
#include "test.h"

int main() {
  yinfo << "yuri is yes" << 5;
  fun();
  yerror << "yuri is yes";
  fun();
  return 0;
}
