/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2025-11-18 15:13:34
 * @LastEditTime: 2025-11-18 16:03:31
 * @Description:
 */
#include "request.hpp"

int main() {
  curl_global_init(CURL_GLOBAL_DEFAULT);
  constexpr auto test_url = "https://cn.apihz.cn/api/ip/shouji.php?id=10004093&key=freeapi&phone=13219931963";

  auto res = CurlRequest::get(test_url);
  yinfo << "res -> " << res;

  // 全局清理
  curl_global_cleanup();
  return 0;
}