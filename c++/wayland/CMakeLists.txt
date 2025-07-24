cmake_minimum_required(VERSION 3.20)

project(HelloWayland)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # 开启生成 compile_commands.json

# 使用 pkg-config 获取版本
find_package(spdlog REQUIRED)
find_package(fmt REQUIRED)

# 打印库路径和版本信息
message(STATUS "WAYLAND_CLIENT_LIBS: ${WAYLAND_CLIENT_LIBRARIES}")
message(STATUS "WAYLAND_CLIENT_VERSION: ${WAYLAND_CLIENT_VERSION}")

add_executable(hello hello.cpp)

# 链接库
# 链接库并传递头文件路径
target_link_libraries(hello PRIVATE 
    spdlog::spdlog 
    fmt::fmt
)

# 确保生成完整的编译命令
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
