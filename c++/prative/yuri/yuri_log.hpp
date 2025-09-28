/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-09-28 08:49:03
 * @LastEditTime: 2025-09-28 09:41:55
 * @Description: 优化的日志库基于c++11，支持更多类型和更美观的输出
 */

#ifndef YURI_LOG_HPP
#define YURI_LOG_HPP

#include <fstream>
#include <iostream>
#include <mutex>
#include <sstream>
#include <ctime>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <list>
#include <deque>
#include <array>
#include <type_traits>
#include <utility>

#ifdef _WIN32
#include <windows.h>
#endif

namespace yuri {

namespace detail {
// SFINAE helpers for container detection
template <typename T>
struct is_container {
  template<typename U>
  static auto test(int) -> decltype(
    std::begin(std::declval<U>()),
    std::end(std::declval<U>()),
    std::true_type{}
  );

  template <typename>
  static std::false_type test(...);

  static constexpr bool value = decltype(test<T>(0))::value;
};

template <typename T>
struct is_pair : std::false_type {};

template <typename K, typename V>
struct is_pair<std::pair<K, V>> : std::true_type {};

template <typename T>
struct is_map_like : std::false_type {};

template <typename K, typename V, typename... Args>
struct is_map_like<std::map<K, V, Args...>> : std::true_type {};

template <typename K, typename V, typename... Args>
struct is_map_like<std::unordered_map<K, V, Args...>> : std::true_type {};
} // namespace detail

class Log final {
public:
    static std::mutex &getMutex() {
    static std::mutex mutex;
    return mutex;
  }

  /**
   * @brief 静态成员函数，用于控制是否将日志写入文件
   */
  static bool &writeInFile() {
    static bool write_in_file = false;
    return write_in_file;
  }

  static std::string &filePath() {
    static std::string path{};
    if (path.empty()) {
      path = "log.txt";
    }
    return path;
  }

  /**
   * @brief 静态成员函数，用于控制是否使用std::cerr输出错误日志
   */
  static bool &useStdError() {
    static bool use_std_cerr = false;
    return use_std_cerr;
  }

private:
  std::ostringstream ost;
  using stringRef = const std::string &;
  bool isError = false;
  static constexpr int INDENT_SIZE = 2;


  void formatMessage() {
    // 添加颜色前缀（仅在控制台输出时）
    if (!writeInFile() && isError) {
      ost << "\x1b[31m"; // 红色
    }

    // 获取当前时间（含毫秒）
    auto now = std::chrono::system_clock::now();
    auto now_time_t = std::chrono::system_clock::to_time_t(now);
    auto now_ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

    // 转换为本地时间
    std::tm localTimeData{};
#ifdef _WIN32
    localtime_s(&localTimeData, &now_time_t);
#else
    localtime_r(&now_time_t, &localTimeData);
#endif

    // 格式化时间（HH:MM:SS）
    char formattedTime[9]; // HH:MM:SS 固定8字符 + 终止符
    std::strftime(formattedTime, sizeof(formattedTime), "%H:%M:%S", &localTimeData);

    // 拼接毫秒（3位）
    ost << "[" << formattedTime << "."
        << now_ms.count() << " "
        << (isError ? "ERROR" : "INFO") << "] ";

#ifdef _WIN32
    // 启用Windows控制台的ANSI转义序列支持
    static bool console_initialized = false;
    if (!console_initialized) {
      const auto hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
      DWORD mode;
      if (GetConsoleMode(hConsole, &mode)) {
        SetConsoleMode(hConsole, mode | ENABLE_VIRTUAL_TERMINAL_PROCESSING);
      }
      console_initialized = true;
    }
#endif
  }

  static void logResult(const std::string &msg, std::ostream &ostream) {
    ostream << msg << std::endl;
  }

  // 格式化容器的辅助函数
  template <typename Container>
  void formatContainer(const Container &container, const std::string &open = "[", const std::string &close = "]") {
    ost << open;
    bool first = true;
    for (const auto &item : container) {
      if (!first) {
        ost << ", ";
      }
      first = false;
      *this << item;
    }
    ost << close;
  }

  // 格式化map类型容器的辅助函数
  template <typename MapContainer>
  void formatMapContainer(const MapContainer &container) {
    ost << "{\n";
    bool first = true;
    for (const auto &pair : container) {
      if (!first) {
        ost << "\n";
      }
      first = false;
      ost << std::string(INDENT_SIZE, ' ') << pair.first << ": ";
      *this << pair.second;
    }
    if (!container.empty()) {
      ost << "\n";
    }
    ost << "}";
  }

public:
  Log(const std::string &func, const int line, bool isError = false) :
    isError(isError) {
    formatMessage();
    ost << func << ":" << line << " -> ";
  }

  explicit Log(const bool isError = false) :
    isError(isError) {
    formatMessage();
  }

  ~Log() {
    std::unique_lock<std::mutex> lock(getMutex());

    // 添加颜色重置（仅在控制台输出时）
    if (!writeInFile()) {
      ost << "\x1b[0m";
    }

    if (writeInFile()) {
      try {
        std::ofstream file(filePath(), std::ios::app);
        if (file.is_open()) {
          file << ost.str() << '\n';
          file.flush();
        }
      } catch (const std::exception &e) {
        std::cerr << "Log file error: " << e.what() << std::endl;
      }
    } else {
      ost << '\n';
      std::ostream &ostream = useStdError() && isError ? std::cerr : std::cout;
      ostream << ost.str();
      ostream.flush();
    }
  }

  // 基础类型输出
  template <typename T>
  Log& operator<<(const T &val) {
    ost << val;
    return *this;
  }

  // std::pair 特化
  template <typename K, typename V>
  Log &operator<<(const std::pair<K, V> &pair) {
    ost << "{" << pair.first << ": " << pair.second << "}";
    return *this;
  }

  // std::vector 特化
  template <typename T, typename Alloc>
  Log &operator<<(const std::vector<T, Alloc> &vec) {
    formatContainer(vec);
    return *this;
  }

  // std::list 特化
  template <typename T, typename Alloc>
  Log &operator<<(const std::list<T, Alloc> &list) {
    formatContainer(list);
    return *this;
  }

  // std::deque 特化
  template <typename T, typename Alloc>
  Log &operator<<(const std::deque<T, Alloc> &deq) {
    formatContainer(deq);
    return *this;
  }

  // std::set 特化
  template <typename T, typename Compare, typename Alloc>
  Log &operator<<(const std::set<T, Compare, Alloc> &set) {
    formatContainer(set, "{", "}");
    return *this;
  }

  // std::unordered_set 特化
  template <typename T, typename Hash, typename KeyEqual, typename Alloc>
  Log &operator<<(const std::unordered_set<T, Hash, KeyEqual, Alloc> &set) {
    formatContainer(set, "{", "}");
    return *this;
  }

  // std::map 特化
  template <typename K, typename V, typename Compare, typename Alloc>
  Log &operator<<(const std::map<K, V, Compare, Alloc> &map) {
    formatMapContainer(map);
    return *this;
  }

  // std::unordered_map 特化
  template <typename K, typename V, typename Hash, typename KeyEqual, typename Alloc>
  Log &operator<<(const std::unordered_map<K, V, Hash, KeyEqual, Alloc> &map) {
    formatMapContainer(map);
    return *this;
  }

  // std::array 特化
  template <typename T, std::size_t N>
  Log &operator<<(const std::array<T, N> &arr) {
    formatContainer(arr);
    return *this;
  }

  Log &operator<<(const bool v) {
    ost << std::boolalpha << v;
    return *this;
  }

};

} // namespace yuri

#ifndef yinfo
#define yinfo ::yuri::Log(__func__, __LINE__, false)
#endif

#ifndef yerror
#define yerror ::yuri::Log(__func__, __LINE__, true)
#endif

#endif /* YURI_LOG_HPP */