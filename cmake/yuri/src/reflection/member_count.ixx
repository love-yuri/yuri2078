export module struct_reflection:members;

import std;

template <typename T>
concept can_init_any = !std::same_as<T, const char *> && !std::same_as<T, std::nullptr_t>;

struct any_type {
  // ReSharper disable once CppFunctionIsNotImplemented
  // ReSharper disable once CppNonExplicitConversionOperator
  template <typename T> requires can_init_any<T>
  [[maybe_unused]] constexpr operator T() const; // NOLINT(*-explicit-constructor)

  // ReSharper disable once CppNonExplicitConversionOperator
  [[maybe_unused]] constexpr operator std::string_view() const {
    return {};
  }
};

/**
 * 递归模板统计T的size
 * @tparam T 模板
 */
template <class T, class... Args>
consteval std::size_t count_members_fn() {
  using V = std::remove_cvref_t<T>;
  if constexpr (requires { V{Args{}..., any_type{}}; }) {
    return count_members_fn<V, Args..., any_type>();
  } else {
    return sizeof...(Args);
  }
}

/**
 *
 * @tparam T
 */
template <class T>
struct ptr_t final {
  const T *ptr;
};

template <size_t N, class T>
constexpr auto get_ptr(T &&t) noexcept {
  auto &p = std::get<N>(to_tie(t));
  return ptr_t<std::remove_cvref_t<decltype(p)>>{&p};
}

template <class T>
extern const T external;

template <auto N, class T>
constexpr std::string_view get_name_impl = member_name<get_ptr<N>(external<std::remove_volatile_t<T>>)>();
