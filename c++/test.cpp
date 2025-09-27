/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-15 21:45:04
 * @LastEditTime: 2025-09-11 20:35:22
 * @Description:
 */

#include <iostream>
#include <bitset>
#include <type_traits>

template <typename T>
void printBinary(T value) {
  if constexpr (std::is_signed_v<T>) {
    // 有符号类型：转换为对应的无符号类型
    using UnsignedType = std::make_unsigned_t<T>;
    std::cout << std::bitset<sizeof(T) * 8>(static_cast<UnsignedType>(value)) << std::endl;
  } else {
    // 无符号类型：直接使用
    std::cout << std::bitset<sizeof(T) * 8>(value) << std::endl;
  }
}

int main() {
  long signedNum = -1;
  unsigned long unsignedNum = 1757504112790 - 1609459200000;

  std::cout << "有符号long: ";
  printBinary(signedNum);

  std::cout << "无符号long: ";
  printBinary(unsignedNum);

  std::string binary_str = "000000000000000000000100000000000000000000000000000000000000000"; // 二进制字符串

  // 使用 bitset 转换
  std::bitset<64> bits(binary_str);
  long result = static_cast<long>(bits.to_ullong());

  std::cout << "二进制: " << binary_str << std::endl;
  std::cout << "十进制: " << result << std::endl;

  std::cout << "左移22位: ";
  printBinary(result);
  std::cout << "左移22位: ";
  printBinary(unsignedNum);

  return 0;
}