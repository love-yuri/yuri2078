/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditTime: 2023-10-12 08:37:07
 * @Description: 测试
 */

#include "yuri_log.hpp"
#include "test.h"

int main() {
  info << "yuri is yes" << 5;
  fun();
  yuri::setWriteInFile();
  error << "yuri is yes";
  fun();
  return 0;
}
