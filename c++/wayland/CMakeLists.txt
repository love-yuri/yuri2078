cmake_minimum_required(VERSION 3.20)

project(HelloWayland)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # 开启生成 compile_commands.json

# 使用 pkg-config 获取版本
find_package(spdlog REQUIRED)
find_package(fmt REQUIRED)
# find_package(waylandpp REQUIRED)
find_package(OpenGL REQUIRED)

# 添加 waylandpp 子项目
add_subdirectory(waylandpp)

add_executable(hello main.cpp)

# 链接库
# 链接库并传递头文件路径
target_link_libraries(hello PRIVATE 
    spdlog::spdlog
    fmt::fmt
    EGL
    wayland-client++
    wayland-egl++
    wayland-cursor++
    wayland-client-extra++
    OpenGL::GL
)

# target_link_libraries(hello PRIVATE
#     /nix/store/pq9lq8iq6cwf1biwf4abwfidrsw2s0kl-waylandpp-1.0.0-dev/lib/libwaylandpp_protocols.so
# )

# 确保生成完整的编译命令
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
target_compile_options(hello PRIVATE -g)

# target_link_libraries(hello PRIVATE waylandpp)