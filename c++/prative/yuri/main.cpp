/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-27 13:29:27
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2023-09-28 13:18:55
 * @FilePath: /learn/c++/prative/yuri/main.cpp
 * @Description:
 *
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
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
