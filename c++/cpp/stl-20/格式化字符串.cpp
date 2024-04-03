#include <yuri/yuri_log.hpp>
#include <format>

template < typename... Args>
void print(const std::string_view fmt_str, Args&&... args) {
  auto fmt_args{std::make_format_args(args...)};
  std::string outstr{ std::vformat(fmt_str, fmt_args) };
  fputs(outstr.c_str(), stdout);
}

struct Frac {
  int a, b;
};

template <typename ...Args>
std::string fun(Args&& ...args) {
  return std::format("hello {} {}", args...);
}

template <>
struct std::formatter<Frac> {
  template <typename ParseContext>
  constexpr auto parse(ParseContext &ctx) {
    return ctx.begin();
  }

  template <typename FormatContextf>
  auto format(const Frac &f, FormatContextf &ctx) const {
    return std::format_to(ctx.out(), "{0:d}/{1:d}", f.a, f.b);
  }
};

int main() {
  yinfo << fun(1, 2);
  Frac f{1, 3};
  print("{}", f);
  return 0;
}
