/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2025-05-22 15:20:19
 * @Description: 测试
 */

#include "yuri_log.hpp"
#include "test.h"

int main() {
  yinfo << "yuri is yes" << 5;
  fun();
  yuri::setWriteInFile();
  yerror << "yuri is yes";
  fun();
  return 0;
}
