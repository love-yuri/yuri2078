/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-10-13 10:15:59
 * @LastEditTime: 2023-10-13 10:54:45
 * @Description: ts基础知识
 */
let str = 'str' // 赋值之后就会给他类型，并且类型是不可变的
// str = 10 报错，不能将number 赋值给 string

let ss: string // 类型注解

/* 可能未定义行为 */
const num = [1, 2, 3, 4, 5]
const ret = num.find(item => item > 2) // find可能未找到
// let sum = ret * 5 报错， ts认为num可能未找到就是undefine
/* 如果确定能够找到这个，可以使用类型断言 */
const ret_2 = num.find(item => item > 2) as number 
let sum = ret_2 * 3 // 成功赋值

/* 基础类型 */
let v0: boolean
let v1: string 
let v2: null
let v3: number
let v4: null
let v5: undefined

/* 联合版本 可以使用多个类型 */
let v6: string | number // 确定类型
let v7: '123' | '345' // 确定数据
let v8: any // 任意类型

/* 数组 */
let array: number[] = [1, 2, 3, 4]
let array_2: Array<string> = ['1', '2', '3', '4']

/* 元组 数据类型确定，且长度确定*/
let yuanzu: [number, string, number] = [1, '2', 3] 
let yurizu_2: [number, number?] = [1, 2] // ?表示可选

/* 枚举类型 两种类型 */
enum Enum {
  a, b, c
}
Enum.a
Enum[0] 

/* 函数 ?可选 ... 剩余参数-> 包装成列表*/
function Myfun(params:string, cho ?: string, ...area:number[]) : string {
  return params;
}

/* 使用泛型 */
function Myfun2<T>(params:T) {
  
}

console.log(Myfun('function'));


/* 接口 */
interface Person {
  name: string
  age: number
  sex: string
}

const person: Person = { name: '', age: 1, sex: '' }
type myT = string | number | boolean // 类型using