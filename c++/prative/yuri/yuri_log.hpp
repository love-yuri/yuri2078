/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-28 08:49:03
 * @LastEditTime: 2025-05-22 15:27:23
 * @Description: 日志库基于c11，可写入文件
 */

#ifndef YURI_LOG_HPP
#define YURI_LOG_HPP

#include <fstream>
#include <iostream>
#include <map>
#include <mutex>
#include <vector>
#include <sstream>
#include <ctime>

#ifdef _WIN32
#include <windows.h>
#endif

namespace yuri {

static std::mutex mutex;
static bool write_in_file = false; // 是否写入文件

/* 将日志结果设置为写入文件 */
static __attribute__((unused))
void setWriteInFile() {
  write_in_file = true;
}

class Log final {
  std::ostringstream ost;
  using stringRef = const std::string &;

  void formatMessage(stringRef func, const int line, bool isError) {
    if (!write_in_file && isError) {
      ost << "\x1b[31m";
    }
    const std::time_t currentTime = std::time(nullptr);
    std::tm localTimeData{};
#ifdef _WIN32
    localtime_s(&localTimeData, &currentTime);
#else
    localtime_r(&currentTime, &localTimeData);
#endif

    char formattedTime[9];
    std::strftime(formattedTime, 9, "%H:%M:%S", &localTimeData);
    ost << "[" << formattedTime << " yuri] " << func << ":" << line << " -> ";
#ifdef _WIN32
    const auto hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD mode;
    GetConsoleMode(hConsole, &mode);
    SetConsoleMode(hConsole, mode | ENABLE_VIRTUAL_TERMINAL_PROCESSING);
#endif
  }

  void logResult(const std::string &msg, std::ostream &ostream) {
    ostream << msg;
    std::endl(ostream);
  }

public:
  Log(const std::string &func, const int line) {
    formatMessage(func, line, false);
  }

  Log(const std::string &func, const int line, bool) {
    formatMessage(func, line, true);
  }

  ~Log() {
    mutex.lock();
    if (write_in_file) {
      try {
        std::fstream fst;
        fst.open("log.txt", std::ios::app);
        logResult(ost.str(), fst);
        fst.flush();
        fst.close();
      } catch (const std::exception &e) {
        std::cout << e.what();
      }
    } else {
      ost << "\x1b[0m";
      logResult(ost.str(), std::cout);
    }
    mutex.unlock();
  }

  template <typename T>
  Log &operator<<(T val) {
    ost << val;
    return *this;
  }

  template <typename T>
  Log &operator<<(const std::vector<T> &vec) {
    *this << "[";
    for (size_t i = 0; i < vec.size(); i++) {
      *this << vec[i];
      if (i != vec.size() - 1) {
        *this << ", ";
      }
    }
    *this << "]\n";
    return *this;
  }

  template <typename KeyVal, typename ValVal>
  Log &operator<<(const std::map<std::vector<KeyVal>, ValVal> &map) {
    *this << "type: Map\n";
    for (auto m : map) {
      *this << m.first << " -> " << m.second << "\n";
    }
    return *this;
  }
};

template <typename T>
std::ostringstream &operator<<(std::ostringstream &os, const std::vector<int> &vec) {
  os << "[";
  for (size_t i = 0; i < vec.size(); i++) {
    os << vec[i];
    if (i != vec.size() - 1) {
      os << ", ";
    }
  }
  os << "]";
  return os;
}

} // namespace yuri

#ifndef yinfo
#define yinfo ::yuri::Log(__func__, __LINE__, false)
#endif

#ifndef yerror
#define yerror ::yuri::Log(__func__, __LINE__, true)
#endif

#endif /* ifndef YURI_LOG_HPP */