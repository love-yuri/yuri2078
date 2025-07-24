/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2025-07-19 21:53:40
 * @LastEditTime: 2025-07-24 19:45:59
 * @Description:
 */
#include "wayland-client.hpp"
#include "wayland-client-protocol-extra.hpp"
#include <cstdint>
#include <fcntl.h>
#include <iostream>
#include <spdlog/spdlog.h>
#include <sys/mman.h>
#include <unistd.h>

using namespace wayland;

int main() {
  display_t display;
  compositor_t compositor;
  buffer_t buffer;
  xdg_wm_base_t wm;
  shm_t shm;
  bool running = true;
  auto registr = display.get_registry();

  /* 绑定全局接口协议 */
  registr.on_global() = [&](uint32_t name, std::string interface, uint32_t version) {
    // spdlog::info("name: {}, interface: {}, version: {}", name, interface, version);
    if (interface == compositor_t::interface_name) {
      registr.bind(name, compositor, version);
    } else if (interface == shm_t::interface_name) {
      registr.bind(name, shm, version);
    } else if (interface == xdg_wm_base_t::interface_name) {
      registr.bind(name, wm, version);
    }
  };

  /* 强制服务器处理请求 */
  display.roundtrip();

  /* 处理心跳检测 */
  wm.on_ping() = [&](uint32_t serial) {
    wm.pong(serial);
  };

  /* 调用混成器创建Surface(基础绘制表面) */
  auto surface = compositor.create_surface();

  /* 调用xgd_shell协议 创建窗口管理 */
  auto xdg_surface = wm.get_xdg_surface(surface);
  auto toplevel = xdg_surface.get_toplevel();

  /* 设置窗口标题以及收到关闭信号时关闭 */
  toplevel.set_title("yuri");
  toplevel.on_close() = [&] {
    spdlog::info("close....");
    running = false;
  };

  /* 创建共享内存 */
  auto shu_name = "shm_yuri_wayland";
  /* 可读可写 | 已经存在则报错 | 不存在则创建 */
  int fd = shm_open(shu_name, O_RDWR | O_EXCL | O_CREAT, 0600);
  if (fd == -1) {
    spdlog::error("创建共享内存失败!!!");
    return -1;
  }

  /* 断开链接，程序结束后自动释放资源 */
  shm_unlink(shu_name);

  /* 给共享内存分配大小 */
  constexpr int width = 300, height = 300;
  constexpr int size = width * height * 4 * 2;
  auto ret = ftruncate(fd, size);
  if (ret < 0) {
    spdlog::error("设置共享内存大小失败!!!");
    return -1;
  }

  /* 映射共享内存到地址空间 */
  void* ptr = mmap(nullptr, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if (ptr == MAP_FAILED) {
    spdlog::error("映射地址空间失败!!");
    return 1;
  }


  /* 创建wayland buffer */
  auto pool = shm.create_pool(fd, size);
  buffer = pool.create_buffer(0, width, height, width * 4, shm_format::xrgb8888);

  auto pixels = static_cast<uint32_t*>(ptr);

  /* 填充颜色 */
  for (int y = 0; y < width; ++y) {
    for (int x = 0; x < height; ++x) {
      if ((x + y / 8 * 8) % 16 < 8) {
        pixels[y * width + x] = 0x333333;
      } else {
        pixels[y * width + x] = 0x333333;
      }
    }
  }

  // 绑定缓冲区到surface
  surface.attach(buffer, 0, 0);

  // 标记整个区域需要重绘
  surface.damage(0, 0, UINT32_MAX, UINT32_MAX);

  // 提交更改
  surface.commit();

  while (running) {
    if (display.dispatch() == -1) {
      break;
    }
  }

  return 0;
}