# Wayland入门

## 数据结构

> 基于waylandpp 进行分析，不对c语言结构进行分析。

### display_t

> 用于连接wayland的， 它代表了 **客户端与 Wayland 服务器的连接**，并管理所有通信

1. **管理 Wayland 连接**
   - 封装了客户端与 Wayland 服务器（如 Hyprland、GNOME Mutter、KWin）的 **Socket 连接**（通常是 Unix Domain Socket，路径类似 `$WAYLAND_DISPLAY`）。
   - 负责 **消息的发送和接收**（Wayland 协议是基于异步事件的）。
2. **事件循环（Event Loop）集成**
   - 提供 `dispatch()` 和 `roundtrip()` 等方法，用于处理来自服务器的事件（如输入事件、窗口状态变化等）。
   - 通常与 `epoll` 或 `libevent` 等事件循环机制配合使用（例如在 GUI 应用中主循环里调用 `wl_display_dispatch()`）。
3. **协议对象管理**
   - 维护所有通过该连接创建的 Wayland 对象（如 `wl_registry`、`wl_surface`、`wl_keyboard` 等）。
   - 在连接断开时自动清理这些资源。
4. **同步控制**
   - `roundtrip()` 方法（如你之前提到的）用于强制同步，确保客户端和服务器的状态一致（例如等待所有全局对象注册完成）。

