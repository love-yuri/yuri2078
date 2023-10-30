#include <iostream>
#include <fstream>
#include <sstream>

int main(int argc, char **argv) {
  if(argc < 2) {
    std::cout << "请输入参数!";
    std::endl(std::cout);
    return -1;
  }
  std::string file(argv[1]);
  std::fstream fs(file, std::ios::in);
  if(!fs.is_open()) {
    std::cout << "文件打开失败!\n";
    return -2;
  }
  std::ostringstream buffer;
  buffer << fs.rdbuf();
  fs.close();
  std::cout << buffer.str() << std::endl;
  return 0;
}
