#include "TcpClient.h"
#include <thread>

void fun(TcpClient *client) {
  while(true) {
    if(client->readFromServer() == false) {
      return;
    }
  }
}

int main() {
  TcpClient client("127.0.0.1", 2078);
  if (client.connect() == false) {
    return 1;
  }
  std::cout << "成功连接服务器! 输入消息按回车结束, 推出请输入bye\n";
  std::thread thread = std::thread(fun, &client);
  while (true) {
    std::string msg;
    std::cin >> msg;
    if (msg == "bye") {
      break;
    }
    client.writeToServer(msg);
  }
  thread.join();
  return 0;
}
