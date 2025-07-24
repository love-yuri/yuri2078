/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2025-07-14 19:35:47
 * @LastEditTime: 2025-07-14 20:34:51
 * @Description:
 */
// main.cpp
#include <spdlog/spdlog.h>

int main() {
    spdlog::info("Welcome to spdlog!");
    spdlog::error("Some error message with arg: {}", 1);
    spdlog::warn("Easy padding in numbers like {:08d}", 12);
    return 0;
}