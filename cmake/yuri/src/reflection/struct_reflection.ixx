export module struct_reflection;

import std;

export namespace yuri::reflection {

/**
 * 最大struct成员数量
 */
constexpr auto max_struct_member_size = 20;

}

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

// 使用结构化绑定获取成员引用

/**
 * 返回t的结构化绑定
 * @tparam T struct类型
 * @tparam N struct成员数量
 */
template <class T, size_t N = count_members_fn<T>()> requires (N < yuri::reflection::max_struct_member_size)
constexpr decltype(auto) tie(T &&t) {
  if constexpr (N == 0) {
    return {};
  } else if constexpr (N == 1) {
    auto &[p] = t;
    return std::tie(p);
  } else if constexpr (N == 2) {
    auto &[p0, p1] = t;
    return std::tie(p0, p1);
  } else if constexpr (N == 3) {
    auto &[p0, p1, p2] = t;
    return std::tie(p0, p1, p2);
  } else if constexpr (N == 4) {
    auto &[p0, p1, p2, p3] = t;
    return std::tie(p0, p1, p2, p3);
  }
}

export namespace yuri::reflection {

/**
 * 获取T的成员数量
 */
template <class T> requires(std::is_aggregate_v<std::remove_cvref_t<T>>)
inline constexpr auto count_members = count_members_fn<T>();

}
