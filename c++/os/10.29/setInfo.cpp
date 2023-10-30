/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-10-29 18:09:48
 * @LastEditTime: 2023-10-29 18:31:02
 * @Description: 设置系统参数
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>

std::unordered_map<std::string, std::string> systemFile;

int main(int argc, char **argv) {
  if (argc < 2) {
    std::cout << "请输入参数!";
    std::endl(std::cout);
    return -1;
  }
  std::string newParam;
  std::cout << "Input " + std::string(argv[1]) + " parameter : ";
  std::cin >> newParam;
  systemFile.insert({"filemax", "/proc/sys/fs/file-max"});
  systemFile.insert({"hostname", "/proc/sys/kernel/hostname"});
  systemFile.insert({"shmmax", "/proc/sys/kernel/shmmax"});
  systemFile.insert({"test", "test.txt"});
  std::string file(systemFile[argv[1]]);
  std::fstream fs;
  fs.open(file, std::ios::in);
  if (!fs.is_open()) {
    std::cout << "文件打开失败!\n";
    return -2;
  }
  std::ostringstream buffer;
  buffer << fs.rdbuf();
  fs.close();
  fs.open(file, std::ios::out | std::ios::trunc);
  if (!fs.is_open()) {
    std::cout << "文件打开失败!\n";
    return -2;
  }
  std::cout << "原来值 -> " << buffer.str() << std::endl;
  fs << newParam;
  fs.close();

  std::cout << "新值 -> " << newParam << std::endl;
  return 0;
}
