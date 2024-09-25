/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-28 08:49:03
 * @LastEditTime: 2024-09-25 13:51:48
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

namespace yuri {

static std::mutex mutex;
static bool write_in_file = false; // 是否写入文件

inline static void logResult(const std::string &msg, std::ostream &cout) {
  cout << msg;
  std::endl(cout);
}

/* 将日志结果设置为写入文件 */
inline static void setWriteInFile() {
  write_in_file = true;
}

class Log {
private:
  std::ostringstream ost;

public:
  Log(const std::string &func, int line) {
    std::time_t currentTime = std::time(nullptr);
    std::tm *localTime = std::localtime(&currentTime);
    char formattedTime[9];
    std::strftime(formattedTime, 9, "%H:%M:%S", localTime);
    ost << formattedTime << " " << func << ":" << line << " -> ";
  }

  Log(const std::string &func, int line, bool) {
    if (!write_in_file) {
      ost << "\x1b[31m";
    }
    std::time_t currentTime = std::time(nullptr);
    std::tm *localTime = std::localtime(&currentTime);
    char formattedTime[9];
    std::strftime(formattedTime, 9, "%H:%M:%S", localTime);
    ost << formattedTime << " " << func << ":" << line << " -> ";
  }

  virtual ~Log() {
    mutex.lock();
    if (write_in_file) {
      std::fstream fst;
      try {
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

  template<typename T>
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
std::ostringstream& operator<<(std::ostringstream &os, const std::vector<int> &vec) {
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

#ifndef info
#define info ::yuri::Log(__func__, __LINE__)
#endif

#ifndef error
#define error ::yuri::Log(__func__, __LINE__, true)
#endif

#endif /* ifndef YURI_LOG_HPP */
