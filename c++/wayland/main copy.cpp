/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2025-07-21 21:03:21
 * @LastEditTime: 2025-07-23 21:13:30
 * @Description:
 */
#include <stdexcept>
#include <iostream>
#include <array>
#include <wayland-client.hpp>
#include <wayland-client-protocol-extra.hpp>
#include <wayland-egl.hpp>
#include <GL/gl.h>
#include <linux/input.h>
#include <wayland-cursor.hpp>
#include <spdlog/spdlog.h>

using namespace wayland;

// helper to create a std::function out of a member function and an object
template <typename R, typename T, typename... Args>
std::function<R(Args...)> bind_mem_fn(R (T::*func)(Args...), T *t) {
  return [func, t](Args... args) {
    return (t->*func)(args...);
  };
}

// example Wayland client
class example {
private:
  // global objects
  display_t display;
  registry_t registry;
  compositor_t compositor;
  shell_t shell;
  xdg_wm_base_t xdg_wm_base;
  seat_t seat;
  shm_t shm;

  // local objects
  surface_t surface;
  xdg_surface_t xdg_surface;
  xdg_toplevel_t xdg_toplevel;
  pointer_t pointer;
  keyboard_t keyboard;
  callback_t frame_cb;
  cursor_image_t cursor_image;
  buffer_t cursor_buffer;
  surface_t cursor_surface;

  // EGL
  egl_window_t egl_window;
  EGLDisplay egldisplay;
  EGLSurface eglsurface;
  EGLContext eglcontext;

  bool running;
  bool has_pointer;
  bool has_keyboard;

  void init_egl() {
    egldisplay = eglGetDisplay(display);
    if (egldisplay == EGL_NO_DISPLAY)
      throw std::runtime_error("eglGetDisplay");

    EGLint major, minor;
    if (eglInitialize(egldisplay, &major, &minor) == EGL_FALSE)
      throw std::runtime_error("eglInitialize");
    if (!((major == 1 && minor >= 4) || major >= 2))
      throw std::runtime_error("EGL version too old");

    if (eglBindAPI(EGL_OPENGL_API) == EGL_FALSE)
      throw std::runtime_error("eglBindAPI");

    std::array<EGLint, 13> config_attribs = {{EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
                                              EGL_RED_SIZE, 8,
                                              EGL_GREEN_SIZE, 8,
                                              EGL_BLUE_SIZE, 8,
                                              EGL_ALPHA_SIZE, 8,
                                              EGL_RENDERABLE_TYPE, EGL_OPENGL_BIT,
                                              EGL_NONE}};

    EGLConfig config;
    EGLint num;
    if (eglChooseConfig(egldisplay, config_attribs.data(), &config, 1, &num) == EGL_FALSE || num == 0)
      throw std::runtime_error("eglChooseConfig");

    std::array<EGLint, 3> context_attribs = {{EGL_CONTEXT_CLIENT_VERSION, 2,
                                              EGL_NONE}};

    eglcontext = eglCreateContext(egldisplay, config, EGL_NO_CONTEXT, context_attribs.data());
    if (eglcontext == EGL_NO_CONTEXT)
      throw std::runtime_error("eglCreateContext");

    eglsurface = eglCreateWindowSurface(egldisplay, config, egl_window, nullptr);
    if (eglsurface == EGL_NO_SURFACE)
      throw std::runtime_error("eglCreateWindowSurface");

    if (eglMakeCurrent(egldisplay, eglsurface, eglsurface, eglcontext) == EGL_FALSE)
      throw std::runtime_error("eglMakeCurrent");
  }

  void draw(uint32_t serial = 0) {
    float h = ((serial >> 4) & 0xFF) / 255.0;
    float s = 1, v = 1;

    int hi = static_cast<int>(h * 6);
    float f = h * 6 - hi;
    float p = v * (1 - s);
    float q = v * (1 - s * f);
    float t = v * (1 - s * (1 - f));
    float r, g, b;

    switch (hi) {
    case 1:
      r = q;
      g = v;
      b = p;
      break;
    case 2:
      r = p;
      g = v;
      b = t;
      break;
    case 3:
      r = p;
      g = q;
      b = v;
      break;
    case 4:
      r = t;
      g = p;
      b = v;
      break;
    case 5:
      r = v;
      g = p;
      b = q;
      break;
    default: // 0,6
      r = v;
      g = t;
      b = p;
      break;
    }

    // draw stuff
    glClearColor(r, g, b, 0.5f);
    glClear(GL_COLOR_BUFFER_BIT);

    // schedule next draw
    frame_cb = surface.frame();
    frame_cb.on_done() = bind_mem_fn(&example::draw, this);

    // swap buffers
    if (eglSwapBuffers(egldisplay, eglsurface) == EGL_FALSE)
      throw std::runtime_error("eglSwapBuffers");
  }

public:
  example() {
    // retrieve global objects
    registry = display.get_registry();

    registry.on_global() = [&](uint32_t name, std::string interface, uint32_t version) {
      // spdlog::info("name: {}, version: {}", interface, version);
      if (interface == compositor_t::interface_name)
        registry.bind(name, compositor, version);
      else if (interface == shell_t::interface_name)
        registry.bind(name, shell, version);
      else if (interface == xdg_wm_base_t::interface_name)
        registry.bind(name, xdg_wm_base, version);
      else if (interface == seat_t::interface_name)
        registry.bind(name, seat, version);
      else if (interface == shm_t::interface_name)
        registry.bind(name, shm, version);
    };
    display.roundtrip();

    seat.on_capabilities() = [&](seat_capability capability) {
      has_keyboard = capability & seat_capability::keyboard;
      has_pointer = capability & seat_capability::pointer;
    };

    // create a surface
    surface = compositor.create_surface();

    // create a shell surface
    if (xdg_wm_base) {
      xdg_wm_base.on_ping() = [&](uint32_t serial) { xdg_wm_base.pong(serial); };
      xdg_surface = xdg_wm_base.get_xdg_surface(surface);
      xdg_surface.on_configure() = [&](uint32_t serial) {
        xdg_surface.ack_configure(serial);
      };
      xdg_toplevel = xdg_surface.get_toplevel();
      xdg_toplevel.set_title("yuri");
      xdg_toplevel.on_close() = [&]() { running = false; };
    }

    surface.commit();

    display.roundtrip();

    // Get input devices
    if (!has_keyboard)
      throw std::runtime_error("No keyboard found.");
    if (!has_pointer)
      throw std::runtime_error("No pointer found.");

    pointer = seat.get_pointer();
    keyboard = seat.get_keyboard();

    // load cursor theme
    cursor_theme_t cursor_theme = cursor_theme_t("default", 16, shm);
    cursor_t cursor = cursor_theme.get_cursor("left_ptr");
    cursor_image = cursor.image(0);
    cursor_buffer = cursor_image.get_buffer();

    // create cursor surface
    cursor_surface = compositor.create_surface();

    // draw cursor
    pointer.on_enter() = [&](uint32_t serial, surface_t, int32_t, int32_t) {
      cursor_surface.attach(cursor_buffer, 0, 0);
      cursor_surface.damage(0, 0, cursor_image.width(), cursor_image.height());
      cursor_surface.commit();
      pointer.set_cursor(serial, cursor_surface, 0, 0);
    };

    // window movement
    pointer.on_button() = [&](uint32_t serial, uint32_t time, uint32_t button, pointer_button_state state) {
      if (button == BTN_LEFT && state == pointer_button_state::pressed) {
        if (xdg_toplevel)
          xdg_toplevel.move(seat, serial);
      }
    };

    // press 'q' to exit
    keyboard.on_key() = [&](uint32_t, uint32_t, uint32_t key, keyboard_key_state state) {
      if (key == KEY_Q && state == keyboard_key_state::pressed)
        running = false;
    };

    // intitialize egl
    egl_window = egl_window_t(surface, 320, 240);
    init_egl();

    // draw stuff
    draw();
  }

  ~example() noexcept(false) {
    // finialize EGL
    if (eglDestroyContext(egldisplay, eglcontext) == EGL_FALSE)
      throw std::runtime_error("eglDestroyContext");
    if (eglTerminate(egldisplay) == EGL_FALSE)
      throw std::runtime_error("eglTerminate");
  }

  void run() {
    // event loop
    running = true;
    while (running)
      display.dispatch();
  }
};

int main() {
  example e;
  e.run();
  return 0;
}
