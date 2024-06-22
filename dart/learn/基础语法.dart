/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-06-17 21:52:04
 * @LastEditTime: 2024-06-17 22:39:56
 * @Description: 基础语法
 */

// 内置数据类型, 所有类型都是引用，不初始化就是null
// 可以加问号表示可空
int num = 10;
double decimal = 10.5;
String str = "Hello";
bool isTrue = true;
List<int> list = [1, 2, 3];
Map<String, int> map = {"a": 1, "b": 2};
var a = "yuri is yes"; // 不指定类型-自动推导-不可改变类型
// dynamic b = "hello"; 使用 dynamic 声明变量，可以改变类型
// Object b = "hello"; 使用 Object 声明变量，可以改变类型
// var1 = 19;

// 常量
const PI = 3.14; // 必须是编译期常量
final name = "yuri"; // 可以是运行时常量

// 类型转换
int num1 = int.parse("10");
double num2 = double.parse("10.5");

// 运算符
void valueFun() {
  Object value = 1 / 2; // 默认数字相除返回double
  value = 1 ~/ 2; // 整除 返回int

  // as 类型转换
  // is 类型判断
  // is! 类型判断

  value = "yuri is yes";
  // 三目运算符
  (value as String).length > 0 ? print("yes") : print("no");

  // 非空条件判断
  var obj = null;
  // 如果为null则返回后面的东西
  value = obj ?? "this is empty";

  // 级联运算符，可以级联调用
  // new Person()..setName("Bob")..setAge(20)..save();

  // 条件成员访问符
  List<String>? list = null;
  // 可以使用非空判断符
  list?.forEach((element) {
    print(element);
  });
  print(list?.length); // 如果list为null则返回null

  print(value);
}

void fun() {
  // 常规函数-int返回值可以省略
  // 不可以指定默认值
  int add(int x, int y) {
    return x + y;
  }

  // 可以指定参数名函数
  // 可以指定默认值
  add2({int x = 0, int y = 0}) {
    return x + y;
  }

  // 效果类似上面的
  // 可选参数
  add3([int x = 0, int y = 0]) {
    return x + y;
  }

  add4(int x, int y) => x + y; // 箭头函数

  print(add(10, 20));
  print(add2(x: 10));
  print(add3());
  print(add4(10, 20));
}

void main(List<String> args) {
  // 打印结果，使用$插值
  print("a: $a");

  valueFun();
}
