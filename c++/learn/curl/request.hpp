#pragma once

#include <curl/curl.h>
#include <string>
#include <string_view>
#include <memory>
#include "yuri_log.hpp"

class CurlRequest {
private:
  std::unique_ptr<CURL, decltype(&curl_easy_cleanup)> curl_ {
    nullptr,
    curl_easy_cleanup
  };

  std::string response_data{};

  // 回调函数，用于接收数据
  static size_t WriteCallback(char *contents, size_t size, size_t nmemb, CurlRequest *request) {
    size_t total_size = size * nmemb;
    request->response_data.append(contents, total_size);
    return total_size;
  }

  // 初始化操作
  bool init() {
    curl_.reset(curl_easy_init());
    if (!curl_) {
      yerror << "Failed to initialize curl!";
      return false;
    }

    // 设置回调函数
    curl_easy_setopt(curl_.get(), CURLOPT_WRITEFUNCTION, &CurlRequest::WriteCallback);
    curl_easy_setopt(curl_.get(), CURLOPT_WRITEDATA, this);

    // 设置一些通用选项
    curl_easy_setopt(curl_.get(), CURLOPT_FOLLOWLOCATION, 1L); // 跟随重定向
    curl_easy_setopt(curl_.get(), CURLOPT_TIMEOUT, 30L);       // 30秒超时

    return true;
  }

public:
  CurlRequest() = default;

  // 禁止拷贝，允许移动
  CurlRequest(const CurlRequest &) = delete;
  CurlRequest &operator=(const CurlRequest &) = delete;
  CurlRequest(CurlRequest &&) = default;
  CurlRequest &operator=(CurlRequest &&) = default;

  // GET 请求
  static std::string get(std::string_view url) {
    CurlRequest request;
    if (!request.init()) {
      yerror << "curl初始化失败!";
      return {};
    }

    // 设置请求 URL (需要null终止的字符串)
    std::string url_str{url};
    curl_easy_setopt(request.curl_.get(), CURLOPT_URL, url_str.c_str());

    // 执行请求
    CURLcode res = curl_easy_perform(request.curl_.get());
    if (res != CURLE_OK) {
      yerror << "GET请求失败: " << curl_easy_strerror(res);
      return {};
    }

    return request.response_data;
  }

  // 为后续的 POST 方法预留接口
  static std::string post(std::string_view url, std::string_view data) {
    CurlRequest request;
    if (!request.init()) {
      yerror << "curl初始化失败!";
      return {};
    }

    std::string url_str{url};
    curl_easy_setopt(request.curl_.get(), CURLOPT_URL, url_str.c_str());
    curl_easy_setopt(request.curl_.get(), CURLOPT_POSTFIELDS, data.data());
    curl_easy_setopt(request.curl_.get(), CURLOPT_POSTFIELDSIZE, data.size());

    CURLcode res = curl_easy_perform(request.curl_.get());
    if (res != CURLE_OK) {
      yerror << "POST请求失败: " << curl_easy_strerror(res);
      return {};
    }

    return request.response_data;
  }
};
