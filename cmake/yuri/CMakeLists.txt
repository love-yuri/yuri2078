cmake_minimum_required(VERSION 4.0)

message("-- Cmake 版本: ${CMAKE_VERSION}")

# vcpkg 和 qt设置
if (WIN32)
  set(CMAKE_PREFIX_PATH "D:\\Qt\\6.8.0\\msvc2022_64\\lib\\cmake")
  if (DEFINED ENV{VCPKG_ROOT})
    set(VCPKG_ROOT $ENV{VCPKG_ROOT})
    message("-- VCPKG_ROOT: $ENV{VCPKG_ROOT}")
  else ()
    set(VCPKG_ROOT "E:/love-yuri/github/vcpkg")
    message(WARNING "-- VCPKG_ROOT 没有设置, 使用默认: ${VCPKG_ROOT}")
  endif ()
  set(CMAKE_TOOLCHAIN_FILE "${VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
endif ()

# 使用import std
set(CMAKE_SUPPRESS_DEVELOPER_WARNINGS 1 CACHE BOOL "Suppress developer warnings")
set(CMAKE_CXX_STANDARD 23)
if (${CMAKE_VERSION} EQUAL "4.2.0")
  set(CMAKE_EXPERIMENTAL_CXX_IMPORT_STD "d0edc3af-4c50-42ea-a356-e2862fe7a444")
elseif (${CMAKE_VERSION} EQUAL "4.0.2")
  set(CMAKE_EXPERIMENTAL_CXX_IMPORT_STD "a9e1cf81-9932-4810-974b-6eccaf14e457")
endif ()
set(CMAKE_CXX_MODULE_STD 1)

# 项目
project(yuri VERSION 1.0 LANGUAGES CXX)

# 配置属性
set(CMAKE_CXX_STANDARD_REQUIRED ON)   # 要求使用指定版本号
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # 开启生成 compile_commands.json

# modules文件检索
file(GLOB IXX_MODULES
    ${PROJECT_SOURCE_DIR}/include/*.ixx
)

file(GLOB_RECURSE PROJECT_SOURCES
    CONFIGURE_DEPENDS
    src/main.cpp
    ${IXX_MODULES}
    ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/include/utils/*.hpp
)

# 生成目标
add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})

# 配置modules支持
target_sources(${PROJECT_NAME}
    PRIVATE
    FILE_SET cxx_modules TYPE CXX_MODULES FILES
    ${IXX_MODULES}
)
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_SCAN_FOR_MODULES ON)

# 包含include目录
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

# MSVC特殊宏
if(MSVC)
  target_compile_options(${PROJECT_NAME} PUBLIC /Zc:preprocessor /utf-8)

  # 关闭 模块未使用utf8编码的异常
  # UTF8 is defined in current command line and not in module command line
  target_compile_options(${PROJECT_NAME} PRIVATE /wd5050)
endif()